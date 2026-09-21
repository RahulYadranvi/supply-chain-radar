from pathlib import Path

from src.parser.markdown_parser import parse_markdown
from src.builder.html_builder import build_html
from src.validator.validator import validate_project, load_metadata

ROOT = Path(__file__).resolve().parent
PROJECTS = ROOT.parent / "00_PROJECT_OS"

EXPORT_HTML = ROOT / "05_EXPORTS" / "html"
EXPORT_HTML.mkdir(parents=True, exist_ok=True)


def build_project(project_path):

    errors = validate_project(project_path)

    if errors:
        print("\nFAILED:", project_path.name)
        for error in errors:
            print(" -", error)
        return

    metadata = load_metadata(project_path)

    md_file = next(project_path.glob("*.md"))

    markdown_text = md_file.read_text(encoding="utf-8")

    html_content = parse_markdown(markdown_text)

    html = build_html(metadata, html_content)

    output = EXPORT_HTML / f"{md_file.stem}.html"

    output.write_text(html, encoding="utf-8")

    print("Generated:", output.name)


def build_all():

    print("\nDOCS_OS Production Builder")
    print("=" * 35)

    projects = sorted(PROJECTS.glob("PROJECT_*"))

    for project in projects:
        build_project(project)

    print("\nDone.")


if __name__ == "__main__":
    build_all()