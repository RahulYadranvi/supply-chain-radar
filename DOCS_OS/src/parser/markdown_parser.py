import markdown

EXTENSIONS = [
    "tables",
    "fenced_code",
    "toc"
]


def parse_markdown(markdown_text: str):
    """Convert Markdown into HTML."""

    html = markdown.markdown(
        markdown_text,
        extensions=EXTENSIONS
    )

    return html