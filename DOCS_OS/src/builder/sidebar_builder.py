from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]

PROJECT_ROOT = ROOT / "00_PROJECT_OS"

DEPARTMENTS = [
    "00_PROJECT_OS",
    "01_COMPANY",
    "02_PRODUCT",
    "03_DESIGN",
    "04_TECHNOLOGY",
    "05_AI_ENGINE",
    "06_DATA",
    "07_INFRASTRUCTURE",
    "08_SECURITY",
    "09_FINANCE",
    "10_MARKETING",
    "11_LEGAL",
    "12_OPERATIONS",
    "13_LAUNCH",
    "14_INVESTORS",
]


def load_department_documents(department_path: Path):
    docs = []

    if not department_path.exists():
        return docs

    for folder in sorted(department_path.glob("PROJECT_*")):
        version = folder / "version.json"

        if version.exists():
            data = json.loads(version.read_text(encoding="utf-8"))

            docs.append(
                {
                    "id": data["document_id"],
                    "title": data["title"],
                    "folder": folder.name,
                    "status": data["status"],
                }
            )

    return docs


def build_sidebar(current_doc=""):
    html = """
<div class="sidebar">

<div class="sidebar-top">

<div class="brand">
<img src="../../assets/icons/logo.svg"/>
<span>Supply Chain Radar</span>
</div>

<div class="search-box">
<input placeholder="Search Docs..." id="searchInput"/>
</div>

</div>

<div class="sidebar-nav">
"""

    for department in DEPARTMENTS:

        html += f'<div class="department">{department.replace("_"," ")}</div>'

        docs = load_department_documents(PROJECT_ROOT / department)

        for doc in docs:

            active = "active" if doc["id"] == current_doc else ""

            html += f"""
<a class="doc-link {active}" href="{doc['folder']}.html">
<div class="doc-title">{doc['title']}</div>
<span class="status {doc['status'].lower()}">{doc['status']}</span>
</a>
"""

    html += """
</div>

<div class="sidebar-footer">
DOCS_OS v1.0
</div>

</div>
"""

    return html