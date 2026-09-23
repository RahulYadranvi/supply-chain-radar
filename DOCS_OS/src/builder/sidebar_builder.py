# ==========================================================
# DOCS_OS Sidebar Builder v2.2
# Restores Original Sidebar + Future TOC Support
# ==========================================================

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = ROOT.parent / "00_PROJECT_OS"

# Fixed department list (always visible)
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


# ==========================================================
# Load Existing Projects
# ==========================================================

def load_projects():

    projects = []

    for folder in sorted(PROJECT_ROOT.glob("PROJECT_*")):

        version_file = folder / "version.json"

        if not version_file.exists():
            continue

        try:
            data = json.loads(version_file.read_text(encoding="utf-8"))
        except Exception:
            continue

        projects.append(
            {
                "id": data.get("document_id", folder.name),
                "title": data.get("title", folder.name),
                "department": data.get("department", "GENERAL"),
            }
        )

    return projects


# ==========================================================
# LEFT SIDEBAR
# ==========================================================

def build_sidebar(current_document):

    projects = load_projects()

    html = """
<aside class="sidebar">

<div class="sidebar-top">

<div class="brand">
<img src="../assets/logo.svg" alt="Logo">
<span>Supply Chain Radar</span>
</div>

<div class="search-box">
<input placeholder="Search Docs..." disabled>
</div>

</div>
"""

    # Always show every department
    for department in DEPARTMENTS:

        html += f"""
<div class="department">
{department.replace("_", " ")}
</div>
"""

        # Show projects only if they belong to this department
        for project in projects:

            if project["department"] != department:
                continue

            active = " active" if project["id"] == current_document else ""

            html += f"""
<a href="{project["id"]}.html" class="doc-link{active}">
    <span class="doc-title">{project["title"]}</span>
</a>
"""

    html += """
<div class="sidebar-footer">
DOCS_OS v1.0
</div>

</aside>
"""

    return html


# ==========================================================
# RIGHT PAGE TOC (used later)
# ==========================================================

def build_page_toc(toc_items):

    if not toc_items:
        return ""

    html = """
<aside class="page-toc">

<div class="page-toc-title">
ON THIS PAGE
</div>
"""

    for item in toc_items:

        cls = "toc-h2" if item["level"] == 2 else "toc-h3"

        html += f"""
<a href="#{item["id"]}" class="toc-link {cls}">
{item["title"]}
</a>
"""

    html += "</aside>"

    return html