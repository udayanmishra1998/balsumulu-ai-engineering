"""
Traceability Manager

Maintains links between artifacts across the ADLC:
  Pain Point → Requirement → Feature (PRD) → Epic → Story

Enables impact analysis when any artifact changes.
"""

from __future__ import annotations

import yaml
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ArtifactLink:
    source_type: str
    source_id: str
    target_type: str
    target_id: str
    relationship: str = "implements"


@dataclass
class TraceabilityMatrix:
    links: list[ArtifactLink] = field(default_factory=list)

    def add_link(
        self,
        source_type: str,
        source_id: str,
        target_type: str,
        target_id: str,
        relationship: str = "implements",
    ):
        link = ArtifactLink(
            source_type=source_type,
            source_id=source_id,
            target_type=target_type,
            target_id=target_id,
            relationship=relationship,
        )
        if not self._link_exists(link):
            self.links.append(link)

    def get_upstream(self, artifact_type: str, artifact_id: str) -> list[ArtifactLink]:
        return [
            link for link in self.links
            if link.target_type == artifact_type and link.target_id == artifact_id
        ]

    def get_downstream(self, artifact_type: str, artifact_id: str) -> list[ArtifactLink]:
        return [
            link for link in self.links
            if link.source_type == artifact_type and link.source_id == artifact_id
        ]

    def impact_analysis(self, artifact_type: str, artifact_id: str) -> dict:
        """Find all artifacts affected if the given artifact changes."""
        affected: dict[str, set[str]] = {}
        visited = set()
        self._find_downstream_recursive(artifact_type, artifact_id, affected, visited)
        return {k: list(v) for k, v in affected.items()}

    def get_full_trace(self, story_id: str) -> dict:
        """Trace a story back to its pain point."""
        trace = {"story": story_id}
        epic_links = self.get_upstream("story", story_id)
        if epic_links:
            trace["epic"] = epic_links[0].source_id
            feature_links = self.get_upstream("epic", trace["epic"])
            if feature_links:
                trace["feature"] = feature_links[0].source_id
                req_links = self.get_upstream("feature", trace["feature"])
                if req_links:
                    trace["requirement"] = req_links[0].source_id
                    pp_links = self.get_upstream("requirement", trace["requirement"])
                    if pp_links:
                        trace["pain_point"] = pp_links[0].source_id
        return trace

    def get_orphans(self, artifact_type: str, all_ids: list[str]) -> list[str]:
        """Find artifacts of a type that have no upstream links."""
        linked_ids = {
            link.target_id for link in self.links
            if link.target_type == artifact_type
        }
        return [aid for aid in all_ids if aid not in linked_ids]

    def _find_downstream_recursive(
        self,
        artifact_type: str,
        artifact_id: str,
        affected: dict[str, set[str]],
        visited: set,
    ):
        key = f"{artifact_type}:{artifact_id}"
        if key in visited:
            return
        visited.add(key)
        downstream = self.get_downstream(artifact_type, artifact_id)
        for link in downstream:
            affected.setdefault(link.target_type, set()).add(link.target_id)
            self._find_downstream_recursive(
                link.target_type, link.target_id, affected, visited
            )

    def _link_exists(self, link: ArtifactLink) -> bool:
        return any(
            existing.source_type == link.source_type
            and existing.source_id == link.source_id
            and existing.target_type == link.target_type
            and existing.target_id == link.target_id
            for existing in self.links
        )


class TraceabilityStore:
    """Persists the traceability matrix for a project."""

    def __init__(self, project_dir: Path):
        self.file = project_dir / "traceability.yaml"
        self.matrix = TraceabilityMatrix()
        self._load()

    def add_link(self, source_type: str, source_id: str, target_type: str, target_id: str, relationship: str = "implements"):
        self.matrix.add_link(source_type, source_id, target_type, target_id, relationship)
        self._save()

    def get_matrix(self) -> TraceabilityMatrix:
        return self.matrix

    def _load(self):
        if self.file.exists():
            with open(self.file) as f:
                data = yaml.safe_load(f) or []
            self.matrix.links = [ArtifactLink(**item) for item in data]

    def _save(self):
        data = [
            {
                "source_type": link.source_type,
                "source_id": link.source_id,
                "target_type": link.target_type,
                "target_id": link.target_id,
                "relationship": link.relationship,
            }
            for link in self.matrix.links
        ]
        with open(self.file, "w") as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)
