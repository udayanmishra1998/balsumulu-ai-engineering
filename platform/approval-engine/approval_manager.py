"""
Approval Engine

Manages milestone approvals, tracks what's pending, and enforces
the human-approval-policy gates.
"""

from __future__ import annotations

import yaml
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Literal


ApprovalStatus = Literal["pending", "approved", "rejected", "revision_requested"]


@dataclass
class ApprovalRequest:
    id: str
    phase: str
    milestone: str
    description: str
    artifacts: list[dict] = field(default_factory=list)
    status: ApprovalStatus = "pending"
    created_at: str = ""
    resolved_at: str | None = None
    founder_notes: str = ""
    revision_count: int = 0

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()


class ApprovalManager:
    """Tracks and enforces approval gates."""

    def __init__(self, project_dir: Path):
        self.project_dir = project_dir
        self.approvals_file = project_dir / "approvals.yaml"
        self.approvals: list[ApprovalRequest] = []
        self._load()

    def request_approval(
        self,
        phase: str,
        milestone: str,
        description: str,
        artifacts: list[dict] | None = None,
    ) -> ApprovalRequest:
        approval_id = f"APR-{phase.upper()[:3]}-{len(self.approvals) + 1:03d}"
        request = ApprovalRequest(
            id=approval_id,
            phase=phase,
            milestone=milestone,
            description=description,
            artifacts=artifacts or [],
        )
        self.approvals.append(request)
        self._save()
        return request

    def approve(self, approval_id: str, notes: str = "") -> ApprovalRequest:
        request = self._find(approval_id)
        if request.status not in ("pending", "revision_requested"):
            raise ValueError(f"Approval {approval_id} is already {request.status}")
        request.status = "approved"
        request.resolved_at = datetime.now().isoformat()
        request.founder_notes = notes
        self._save()
        return request

    def reject(self, approval_id: str, reason: str = "") -> ApprovalRequest:
        request = self._find(approval_id)
        request.status = "rejected"
        request.resolved_at = datetime.now().isoformat()
        request.founder_notes = reason
        self._save()
        return request

    def request_revision(self, approval_id: str, feedback: str = "") -> ApprovalRequest:
        request = self._find(approval_id)
        request.status = "revision_requested"
        request.founder_notes = feedback
        request.revision_count += 1
        request.resolved_at = None
        self._save()
        return request

    def resubmit(self, approval_id: str, updated_artifacts: list[dict] | None = None) -> ApprovalRequest:
        request = self._find(approval_id)
        if request.status != "revision_requested":
            raise ValueError(f"Approval {approval_id} is not in revision_requested state")
        request.status = "pending"
        if updated_artifacts:
            request.artifacts = updated_artifacts
        self._save()
        return request

    def get_pending(self) -> list[ApprovalRequest]:
        return [a for a in self.approvals if a.status in ("pending", "revision_requested")]

    def get_phase_approvals(self, phase: str) -> list[ApprovalRequest]:
        return [a for a in self.approvals if a.phase == phase]

    def is_phase_fully_approved(self, phase: str) -> bool:
        phase_approvals = self.get_phase_approvals(phase)
        if not phase_approvals:
            return False
        return all(a.status == "approved" for a in phase_approvals)

    def get_approval_summary(self) -> dict:
        return {
            "total": len(self.approvals),
            "pending": len([a for a in self.approvals if a.status == "pending"]),
            "approved": len([a for a in self.approvals if a.status == "approved"]),
            "rejected": len([a for a in self.approvals if a.status == "rejected"]),
            "revision_requested": len([a for a in self.approvals if a.status == "revision_requested"]),
            "by_phase": {
                phase: {
                    "count": len(approvals),
                    "approved": len([a for a in approvals if a.status == "approved"]),
                }
                for phase, approvals in self._group_by_phase().items()
            },
        }

    def _find(self, approval_id: str) -> ApprovalRequest:
        for a in self.approvals:
            if a.id == approval_id:
                return a
        raise ValueError(f"Approval {approval_id} not found")

    def _group_by_phase(self) -> dict[str, list[ApprovalRequest]]:
        groups: dict[str, list[ApprovalRequest]] = {}
        for a in self.approvals:
            groups.setdefault(a.phase, []).append(a)
        return groups

    def _load(self):
        if self.approvals_file.exists():
            with open(self.approvals_file) as f:
                data = yaml.safe_load(f) or []
            self.approvals = [ApprovalRequest(**item) for item in data]

    def _save(self):
        self.project_dir.mkdir(parents=True, exist_ok=True)
        data = [
            {
                "id": a.id,
                "phase": a.phase,
                "milestone": a.milestone,
                "description": a.description,
                "artifacts": a.artifacts,
                "status": a.status,
                "created_at": a.created_at,
                "resolved_at": a.resolved_at,
                "founder_notes": a.founder_notes,
                "revision_count": a.revision_count,
            }
            for a in self.approvals
        ]
        with open(self.approvals_file, "w") as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)
