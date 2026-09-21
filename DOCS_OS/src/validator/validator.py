import json
from pathlib import Path


REQUIRED_KEYS = [
    "document_id",
    "title",
    "version",
    "status",
    "owner",
    "department",
    "created",
    "last_updated",
    "generator"
]


def validate_project(project_path: Path):
    errors = []

    md_files = list(project_path.glob("*.md"))

    if len(md_files) != 1:
        errors.append("Exactly one markdown file is required.")

    version_file = project_path / "version.json"

    if not version_file.exists():
        errors.append("Missing required file: version.json")

    return errors


def load_metadata(project_path: Path):
    version_file = project_path / "version.json"

    data = json.loads(version_file.read_text(encoding="utf-8"))

    for key in REQUIRED_KEYS:
        if key not in data:
            raise ValueError(f"Missing metadata field: {key}")

    return {
        "Document ID": data["document_id"],
        "Title": data["title"],
        "Version": data["version"],
        "Status": data["status"],
        "Owner": data["owner"],
        "Department": data["department"],
        "Created": data["created"],
        "Last Updated": data["last_updated"],
        "Documentation Engine": data["generator"]
    }