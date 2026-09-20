from pathlib import Path
import json
import markdown

ROOT = Path(__file__).parent
CONFIG_DIR = ROOT / "04_GENERATORS" / "config"

with open(CONFIG_DIR / "config.json", "r", encoding="utf-8") as f:
    CONFIG = json.load(f)

with open(CONFIG_DIR / "theme.json", "r", encoding="utf-8") as f:
    THEME = json.load(f)


def build(markdown_file: str):
    md_path = Path(markdown_file)

    if not md_path.exists():
        print(f"❌ File not found: {md_path}")
        return

    output_dir = ROOT / "05_EXPORTS" / "html"
    output_dir.mkdir(parents=True, exist_ok=True)

    html_body = markdown.markdown(
        md_path.read_text(encoding="utf-8"),
        extensions=["tables", "fenced_code", "toc"]
    )

    html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{CONFIG['project_name']}</title>

<style>
body{{
    margin:auto;
    background:{THEME['background_color']};
    color:{THEME['text_color']};
    font-family:Arial, sans-serif;
    max-width:{THEME['page_width']};
    padding:50px;
    line-height:1.8;
}}

h1,h2,h3{{
    color:{THEME['primary_color']};
}}

pre{{
    background:#1E293B;
    padding:15px;
    border-radius:12px;
    overflow:auto;
}}

table{{
    border-collapse:collapse;
    width:100%;
}}

th,td{{
    border:1px solid #334155;
    padding:12px;
}}
</style>

</head>

<body>
{html_body}
</body>
</html>
"""

    output_file = output_dir / f"{md_path.stem}.html"
    output_file.write_text(html, encoding="utf-8")

    print(f"✅ Generated: {output_file}")


if __name__ == "__main__":
    build("06_EXAMPLES/PROJECT_SAMPLE.md")