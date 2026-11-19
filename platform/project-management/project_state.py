"""
Project State Management

Manages the state of a project as it moves through ADLC phases.
State is persisted as YAML files in the project's local directory.
"""

from __future__ import annotations

import yaml
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Literal


Phase = Literal[
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

Status = Literal["not_started", "in_progress", "pending_approval", "approved", "rejected"]


@dataclass
class ActivityState:
    name: str
    status: Status = "not_started"
    started_at: str | None = None
    completed_at: str | None = None
    artifacts: list[dict] = field(default_factory=list)
    notes: str = ""


@dataclass
class PhaseState:
    phase: Phase
    status: Status = "not_started"
    started_at: str | None = None
    completed_at: str | None = None
    activities: list[ActivityState] = field(default_factory=list)
    approval: dict | None = None


@dataclass
class ProjectState:
    project_name: str
    current_phase: Phase = "discovery"
    created_at: str = ""
    updated_at: str = ""
    phases: dict[str, PhaseState] = field(default_factory=dict)
    config: dict = field(default_factory=dict)

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()
        if not self.phases:
            for phase in Phase.__args__:
                self.phases[phase] = PhaseState(phase=phase)


class ProjectStateManager:
    """Manages project state persistence and transitions."""

    def __init__(self, project_dir: Path):
        self.project_dir = project_dir
        self.state_file = project_dir / "state.yaml"
        self.state: ProjectState | None = None

    def initialize(self, project_name: str, config: dict | None = None) -> ProjectState:
        self.project_dir.mkdir(parents=True, exist_ok=True)
        self.state = ProjectState(
            project_name=project_name,
            config=config or {},
        )
        self._save()
        return self.state

    def load(self) -> ProjectState:
        if not self.state_file.exists():
            raise FileNotFoundError(f"No project state found at {self.state_file}")
        with open(self.state_file) as f:
            data = yaml.safe_load(f)
        self.state = self._from_dict(data)
        return self.state

    def get_current_phase(self) -> PhaseState:
        self._ensure_loaded()
        return self.state.phases[self.state.current_phase]

    def get_current_activity(self) -> ActivityState | None:
        phase = self.get_current_phase()
        for activity in phase.activities:
            if activity.status == "in_progress":
                return activity
        return None

    def start_phase(self, phase: Phase) -> PhaseState:
        self._ensure_loaded()
        phase_state = self.state.phases[phase]
        if phase_state.status not in ("not_started", "rejected"):
            raise ValueError(f"Phase {phase} is already {phase_state.status}")
        phase_state.status = "in_progress"
        phase_state.started_at = datetime.now().isoformat()
        self.state.current_phase = phase
        self._save()
        return phase_state

    def start_activity(self, activity_name: str) -> ActivityState:
        self._ensure_loaded()
        phase = self.get_current_phase()
        activity = ActivityState(
            name=activity_name,
            status="in_progress",
            started_at=datetime.now().isoformat(),
        )
        phase.activities.append(activity)
        self._save()
        return activity

    def complete_activity(self, activity_name: str, artifacts: list[dict] | None = None) -> ActivityState:
        self._ensure_loaded()
        phase = self.get_current_phase()
        for activity in phase.activities:
            if activity.name == activity_name and activity.status == "in_progress":
                activity.status = "approved"
                activity.completed_at = datetime.now().isoformat()
                if artifacts:
                    activity.artifacts = artifacts
                self._save()
                return activity
        raise ValueError(f"No in-progress activity named {activity_name}")

    def submit_for_approval(self, phase: Phase | None = None) -> PhaseState:
        self._ensure_loaded()
        phase_name = phase or self.state.current_phase
        phase_state = self.state.phases[phase_name]
        phase_state.status = "pending_approval"
        self._save()
        return phase_state

    def approve_phase(self, phase: Phase | None = None, notes: str = "") -> PhaseState:
        self._ensure_loaded()
        phase_name = phase or self.state.current_phase
        phase_state = self.state.phases[phase_name]
        if phase_state.status != "pending_approval":
            raise ValueError(f"Phase {phase_name} is not pending approval")
        phase_state.status = "approved"
        phase_state.completed_at = datetime.now().isoformat()
        phase_state.approval = {
            "approved_at": datetime.now().isoformat(),
            "notes": notes,
        }
        self._save()
        return phase_state

    def reject_phase(self, phase: Phase | None = None, reason: str = "") -> PhaseState:
        self._ensure_loaded()
        phase_name = phase or self.state.current_phase
        phase_state = self.state.phases[phase_name]
        phase_state.status = "rejected"
        phase_state.approval = {
            "rejected_at": datetime.now().isoformat(),
            "reason": reason,
        }
        self._save()
        return phase_state

    def can_transition_to(self, target_phase: Phase) -> tuple[bool, str]:
        """Check if the project can move to the target phase."""
        self._ensure_loaded()
        phase_order = list(Phase.__args__)
        current_idx = phase_order.index(self.state.current_phase)
        target_idx = phase_order.index(target_phase)

        if target_idx > current_idx + 1:
            return False, f"Cannot skip phases. Current: {self.state.current_phase}, Target: {target_phase}"

        current_phase = self.state.phases[self.state.current_phase]
        if current_phase.status != "approved":
            return False, f"Current phase '{self.state.current_phase}' must be approved before transitioning"

        return True, "Transition allowed"

    def get_summary(self) -> dict:
        self._ensure_loaded()
        return {
            "project": self.state.project_name,
            "current_phase": self.state.current_phase,
            "phase_status": self.state.phases[self.state.current_phase].status,
            "current_activity": (
                self.get_current_activity().name if self.get_current_activity() else None
            ),
            "phases": {
                name: {"status": ps.status, "activities": len(ps.activities)}
                for name, ps in self.state.phases.items()
                if ps.status != "not_started"
            },
        }

    def _ensure_loaded(self):
        if self.state is None:
            self.load()

    def _save(self):
        self.state.updated_at = datetime.now().isoformat()
        with open(self.state_file, "w") as f:
            yaml.dump(self._to_dict(self.state), f, default_flow_style=False, sort_keys=False)

    def _to_dict(self, obj) -> dict:
        if isinstance(obj, dict):
            return {k: self._to_dict(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [self._to_dict(v) for v in obj]
        if hasattr(obj, "__dataclass_fields__"):
            return {k: self._to_dict(v) for k, v in asdict(obj).items()}
        return obj

    def _from_dict(self, data: dict) -> ProjectState:
        phases = {}
        for name, phase_data in data.get("phases", {}).items():
            activities = [
                ActivityState(**a) for a in phase_data.pop("activities", [])
            ]
            phases[name] = PhaseState(**phase_data, activities=activities)
        data["phases"] = phases
        return ProjectState(**data)
