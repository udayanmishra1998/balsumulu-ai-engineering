"""
Workflow Executor

Executes workflow definitions by coordinating agents, skills, state
transitions, and HITL checkpoints. This is the engine that drives
the ADLC pipeline.

The executor is designed to be called by the AI editor (Claude Code,
Cursor, etc.) — it manages state and provides the next step, while
the editor provides the intelligence.
"""

from __future__ import annotations

import yaml
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Literal


StepStatus = Literal["pending", "in_progress", "waiting_approval", "approved", "skipped", "failed"]


@dataclass
class WorkflowStep:
    id: str
    name: str
    agent: str
    skill: str
    description: str
    hitl_required: bool = False
    hitl_description: str = ""
    status: StepStatus = "pending"
    started_at: str | None = None
    completed_at: str | None = None
    outputs: list[dict] = field(default_factory=list)
    notes: str = ""


@dataclass
class WorkflowInstance:
    workflow_name: str
    project_name: str
    steps: list[WorkflowStep] = field(default_factory=list)
    current_step_index: int = 0
    status: str = "not_started"
    started_at: str = ""
    completed_at: str | None = None


class WorkflowExecutor:
    """Drives a workflow through its steps, managing state and HITL gates."""

    def __init__(self, project_dir: Path):
        self.project_dir = project_dir
        self.workflows_dir = project_dir / "workflows"
        self.workflows_dir.mkdir(parents=True, exist_ok=True)

    def start_workflow(self, workflow_name: str, project_name: str, steps: list[dict]) -> WorkflowInstance:
        workflow = WorkflowInstance(
            workflow_name=workflow_name,
            project_name=project_name,
            steps=[WorkflowStep(**step) for step in steps],
            status="in_progress",
            started_at=datetime.now().isoformat(),
        )
        if workflow.steps:
            workflow.steps[0].status = "in_progress"
            workflow.steps[0].started_at = datetime.now().isoformat()
        self._save_workflow(workflow)
        return workflow

    def get_workflow(self, workflow_name: str) -> WorkflowInstance:
        return self._load_workflow(workflow_name)

    def get_current_step(self, workflow_name: str) -> WorkflowStep | None:
        workflow = self._load_workflow(workflow_name)
        if workflow.current_step_index < len(workflow.steps):
            return workflow.steps[workflow.current_step_index]
        return None

    def get_next_action(self, workflow_name: str) -> dict:
        """Returns what the AI editor should do next."""
        workflow = self._load_workflow(workflow_name)
        current = self.get_current_step(workflow_name)

        if current is None:
            return {"action": "workflow_complete", "workflow": workflow_name}

        if current.status == "waiting_approval":
            return {
                "action": "waiting_approval",
                "step": current.name,
                "description": current.hitl_description,
                "approval_id": current.id,
            }

        if current.status == "in_progress":
            return {
                "action": "execute_step",
                "step": current.name,
                "agent": current.agent,
                "skill": current.skill,
                "description": current.description,
            }

        if current.status == "pending":
            current.status = "in_progress"
            current.started_at = datetime.now().isoformat()
            self._save_workflow(workflow)
            return {
                "action": "execute_step",
                "step": current.name,
                "agent": current.agent,
                "skill": current.skill,
                "description": current.description,
            }

        return {"action": "unknown_state", "step_status": current.status}

    def complete_step(
        self,
        workflow_name: str,
        outputs: list[dict] | None = None,
        notes: str = "",
    ) -> dict:
        """Mark the current step as complete and advance."""
        workflow = self._load_workflow(workflow_name)
        current = workflow.steps[workflow.current_step_index]

        if current.hitl_required:
            current.status = "waiting_approval"
            current.outputs = outputs or []
            current.notes = notes
            self._save_workflow(workflow)
            return {
                "action": "approval_needed",
                "step": current.name,
                "description": current.hitl_description,
            }

        current.status = "approved"
        current.completed_at = datetime.now().isoformat()
        current.outputs = outputs or []
        current.notes = notes

        return self._advance(workflow)

    def approve_step(self, workflow_name: str, notes: str = "") -> dict:
        """Founder approves the current step."""
        workflow = self._load_workflow(workflow_name)
        current = workflow.steps[workflow.current_step_index]

        if current.status != "waiting_approval":
            raise ValueError(f"Step {current.name} is not waiting for approval")

        current.status = "approved"
        current.completed_at = datetime.now().isoformat()
        current.notes = notes

        return self._advance(workflow)

    def reject_step(self, workflow_name: str, feedback: str = "") -> dict:
        """Founder rejects, step needs rework."""
        workflow = self._load_workflow(workflow_name)
        current = workflow.steps[workflow.current_step_index]
        current.status = "in_progress"
        current.notes = f"Revision requested: {feedback}"
        self._save_workflow(workflow)
        return {
            "action": "revision_needed",
            "step": current.name,
            "feedback": feedback,
        }

    def get_progress(self, workflow_name: str) -> dict:
        workflow = self._load_workflow(workflow_name)
        total = len(workflow.steps)
        completed = len([s for s in workflow.steps if s.status == "approved"])
        return {
            "workflow": workflow_name,
            "status": workflow.status,
            "progress": f"{completed}/{total}",
            "current_step": (
                workflow.steps[workflow.current_step_index].name
                if workflow.current_step_index < total
                else "complete"
            ),
            "steps": [
                {"name": s.name, "status": s.status}
                for s in workflow.steps
            ],
        }

    def _advance(self, workflow: WorkflowInstance) -> dict:
        workflow.current_step_index += 1
        if workflow.current_step_index >= len(workflow.steps):
            workflow.status = "completed"
            workflow.completed_at = datetime.now().isoformat()
            self._save_workflow(workflow)
            return {"action": "workflow_complete", "workflow": workflow.workflow_name}

        next_step = workflow.steps[workflow.current_step_index]
        next_step.status = "in_progress"
        next_step.started_at = datetime.now().isoformat()
        self._save_workflow(workflow)
        return {
            "action": "next_step",
            "step": next_step.name,
            "agent": next_step.agent,
            "skill": next_step.skill,
            "description": next_step.description,
        }

    def _save_workflow(self, workflow: WorkflowInstance):
        file = self.workflows_dir / f"{workflow.workflow_name}.yaml"
        data = {
            "workflow_name": workflow.workflow_name,
            "project_name": workflow.project_name,
            "status": workflow.status,
            "started_at": workflow.started_at,
            "completed_at": workflow.completed_at,
            "current_step_index": workflow.current_step_index,
            "steps": [
                {
                    "id": s.id,
                    "name": s.name,
                    "agent": s.agent,
                    "skill": s.skill,
                    "description": s.description,
                    "hitl_required": s.hitl_required,
                    "hitl_description": s.hitl_description,
                    "status": s.status,
                    "started_at": s.started_at,
                    "completed_at": s.completed_at,
                    "outputs": s.outputs,
                    "notes": s.notes,
                }
                for s in workflow.steps
            ],
        }
        with open(file, "w") as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)

    def _load_workflow(self, workflow_name: str) -> WorkflowInstance:
        file = self.workflows_dir / f"{workflow_name}.yaml"
        if not file.exists():
            raise FileNotFoundError(f"Workflow {workflow_name} not found")
        with open(file) as f:
            data = yaml.safe_load(f)
        steps = [WorkflowStep(**s) for s in data.pop("steps", [])]
        return WorkflowInstance(**data, steps=steps)
