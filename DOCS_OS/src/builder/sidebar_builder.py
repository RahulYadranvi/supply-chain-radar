from pathlib import Path


def build_sidebar(projects_root: Path) -> str:
    """
    Generates sidebar HTML listing every project.
    """

    items = []

    projects = sorted(projects_root.glob("PROJECT_*"))

    for project in projects:
        title = project.name.replace("_", " ")
        slug = project.name + ".html"

        items.append(
            f"""
            <li class="sidebar-item">
                <a href="{slug}">{title}</a>
            </li>
            """
        )

    return f"""
    <aside class="sidebar">
        <div class="sidebar-header">
            <h2>DOCS_OS</h2>
            <span>Navigation</span>
        </div>

        <ul class="sidebar-list">
            {''.join(items)}
        </ul>
    </aside>
    """