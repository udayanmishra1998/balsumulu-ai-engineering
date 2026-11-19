"""
ADLC State Machine

Defines the state machine for the Agent Development Life Cycle.
Manages phase transitions, quality gate enforcement, and routing
to the correct workflow/agent/skill at each step.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from platform.project_management.project_state import ProjectStateManager, Phase
from platform.approval_engine.approval_manager import ApprovalManager
from platform.workflow_engine.workflow_executor import WorkflowExecutor


@dataclass
class QualityGate:
    phase: str
    checks: list[str]
    description: str


PHASE_1_GATES: dict[str, QualityGate] = {
    "discovery": QualityGate(
        phase="discovery",
        description="Discovery quality gate",
        checks=[
            "problem_statement_defined",
            "market_research_complete",
            "target_users_identified",
            "value_proposition_clear",
            "product_vision_approved",
            "success_metrics_defined",
        ],
    ),
    "requirements": QualityGate(
        phase="requirements",
        description="Requirements quality gate",
        checks=[
            "personas_defined",
            "user_journeys_mapped",
            "features_linked_to_personas",
            "requirements_have_ids_and_priorities",
            "moscow_complete",
            "mvp_boundary_defined",
            "nfr_captured",
        ],
    ),
    "specification": QualityGate(
        phase="specification",
        description="Specification quality gate",
        checks=[
            "all_mvp_features_specified",
            "acceptance_criteria_per_feature",
            "all_acs_testable",
            "nfr_measurable_targets",
            "integrations_specified",
            "no_tbd_sections",
            "prd_published",
        ],
    ),
    "planning": QualityGate(
        phase="planning",
        description="Planning quality gate",
        checks=[
            "roadmap_defined",
            "epics_decomposed",
            "stories_follow_invest",
            "stories_have_acceptance_criteria",
            "dependencies_mapped",
            "priority_order_approved",
            "backlog_in_tool",
        ],
    ),
}

PHASE_WORKFLOWS: dict[str, list[str]] = {
    "discovery": [
        "discussion-to-product-requirements",
        "research-to-product-strategy",
    ],
    "requirements": [
        "discussion-to-product-requirements",
    ],
    "specification": [
        "requirements-to-prd",
    ],
    "planning": [
        "prd-to-architecture",
        "architecture-to-backlog",
    ],
}

PHASE_AGENTS: dict[str, list[str]] = {
    "discovery": ["product-analyst", "research-analyst"],
    "requirements": ["requirements-analyst"],
    "specification": ["prd-agent"],
    "planning": ["engineering-planner"],
}

PHASE_ORDER: list[Phase] = [
    "discovery",
    "requirements",
    "specification",
    "planning",
    "architecture",
    "implementation",
    "testing",
    "release",
    "operations",
]


class ADLCOrchestrator:
    """
    Orchestrates the ADLC pipeline for a project.

    This is the main entry point the MCP server uses to drive the harness.
    It coordinates state management, approval gates, workflow execution,
    and provides the AI editor with what to do next.
    """

    def __init__(self, project_dir: Path):
        self.project_dir = project_dir
        self.state_manager = ProjectStateManager(project_dir)
        self.approval_manager = ApprovalManager(project_dir)
        self.workflow_executor = WorkflowExecutor(project_dir)

    def initialize_project(self, project_name: str, config: dict | None = None) -> dict:
        state = self.state_manager.initialize(project_name, config)
        self.state_manager.start_phase("discovery")
        return {
            "status": "initialized",
            "project": project_name,
            "current_phase": "discovery",
            "next_action": "Start idea intake with the Product Analyst using the product-discovery skill.",
            "agents": PHASE_AGENTS["discovery"],
            "workflows": PHASE_WORKFLOWS["discovery"],
        }

    def get_status(self) -> dict:
        summary = self.state_manager.get_summary()
        approval_summary = self.approval_manager.get_approval_summary()
        pending = self.approval_manager.get_pending()

        result = {
            **summary,
            "approvals": approval_summary,
        }

        if pending:
            result["pending_approvals"] = [
                {"id": a.id, "milestone": a.milestone, "description": a.description}
                for a in pending
            ]

        return result

    def get_next_action(self) -> dict:
        state = self.state_manager.load()
        current_phase = state.phases[state.current_phase]

        pending = self.approval_manager.get_pending()
        if pending:
            return {
                "action": "waiting_approval",
                "approvals": [
                    {"id": a.id, "milestone": a.milestone, "description": a.description}
                    for a in pending
                ],
                "message": "Waiting for founder approval before proceeding.",
            }

        if current_phase.status == "approved":
            next_phase = self._get_next_phase(state.current_phase)
            if next_phase:
                return {
                    "action": "ready_for_next_phase",
                    "current_phase": state.current_phase,
                    "next_phase": next_phase,
                    "agents": PHASE_AGENTS.get(next_phase, []),
                    "workflows": PHASE_WORKFLOWS.get(next_phase, []),
                    "message": f"Phase '{state.current_phase}' is approved. Ready to start '{next_phase}'.",
                }
            return {
                "action": "pipeline_complete",
                "message": "All phases complete. The backlog is ready for a technical architect.",
            }

        if current_phase.status == "in_progress":
            current_activity = self.state_manager.get_current_activity()
            return {
                "action": "continue_phase",
                "phase": state.current_phase,
                "current_activity": current_activity.name if current_activity else None,
                "agents": PHASE_AGENTS.get(state.current_phase, []),
                "workflows": PHASE_WORKFLOWS.get(state.current_phase, []),
                "message": f"Continue working on '{state.current_phase}' phase.",
            }

        if current_phase.status == "not_started":
            return {
                "action": "start_phase",
                "phase": state.current_phase,
                "agents": PHASE_AGENTS.get(state.current_phase, []),
                "workflows": PHASE_WORKFLOWS.get(state.current_phase, []),
            }

        return {"action": "unknown", "phase_status": current_phase.status}

    def submit_milestone(self, milestone: str, description: str, artifacts: list[dict] | None = None) -> dict:
        state = self.state_manager.load()
        approval = self.approval_manager.request_approval(
            phase=state.current_phase,
            milestone=milestone,
            description=description,
            artifacts=artifacts,
        )
        self.state_manager.submit_for_approval()
        return {
            "approval_id": approval.id,
            "status": "pending",
            "message": f"Milestone '{milestone}' submitted for founder approval.",
        }

    def founder_approve(self, approval_id: str, notes: str = "") -> dict:
        approval = self.approval_manager.approve(approval_id, notes)

        if self.approval_manager.is_phase_fully_approved(approval.phase):
            self.state_manager.approve_phase(approval.phase, notes)
            next_phase = self._get_next_phase(approval.phase)
            return {
                "status": "phase_approved",
                "phase": approval.phase,
                "next_phase": next_phase,
                "message": f"Phase '{approval.phase}' fully approved.",
            }

        return {
            "status": "milestone_approved",
            "milestone": approval.milestone,
            "message": f"Milestone approved. Continue with the current phase.",
        }

    def founder_reject(self, approval_id: str, reason: str = "") -> dict:
        approval = self.approval_manager.reject(approval_id, reason)
        self.state_manager.reject_phase(approval.phase, reason)
        return {
            "status": "rejected",
            "milestone": approval.milestone,
            "reason": reason,
            "message": "Revise and resubmit based on feedback.",
        }

    def advance_to_phase(self, target_phase: Phase) -> dict:
        can_transition, reason = self.state_manager.can_transition_to(target_phase)
        if not can_transition:
            return {"status": "blocked", "reason": reason}

        self.state_manager.start_phase(target_phase)
        return {
            "status": "advanced",
            "phase": target_phase,
            "agents": PHASE_AGENTS.get(target_phase, []),
            "workflows": PHASE_WORKFLOWS.get(target_phase, []),
            "message": f"Advanced to '{target_phase}' phase.",
        }

    def check_quality_gate(self, phase: str) -> dict:
        gate = PHASE_1_GATES.get(phase)
        if not gate:
            return {"status": "no_gate", "phase": phase}

        return {
            "phase": phase,
            "gate": gate.description,
            "checks": gate.checks,
            "message": "Review each check with the founder before approving the phase.",
        }

    def _get_next_phase(self, current: str) -> str | None:
        try:
            idx = PHASE_ORDER.index(current)
            if idx + 1 < len(PHASE_ORDER):
                return PHASE_ORDER[idx + 1]
        except ValueError:
            pass
        return None
