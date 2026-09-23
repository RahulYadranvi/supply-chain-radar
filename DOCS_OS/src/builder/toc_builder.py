import re
from html import escape

# ==========================================================
# DOCS_OS TOC Builder v1.0
# ==========================================================

HEADING_PATTERN = re.compile(
    r"<h([23])>(.*?)</h\1>",
    re.IGNORECASE | re.DOTALL,
)


def slugify(text: str) -> str:
    """
    Convert heading text into a URL-friendly anchor.

    Example:
    'Chapter 1 — Documentation Philosophy'
    -> 'chapter-1-documentation-philosophy'
    """

    text = re.sub(r"<.*?>", "", text)
    text = text.lower()

    text = re.sub(r"[—–-]+", "-", text)
    text = re.sub(r"[^a-z0-9\\s-]", "", text)
    text = re.sub(r"\\s+", "-", text)
    text = re.sub(r"-+", "-", text)

    return text.strip("-")


def build_toc(html: str):
    """
    Returns:
        updated_html
        toc_items
    """

    toc = []

    def replace_heading(match):

        level = int(match.group(1))
        title = re.sub(r"<.*?>", "", match.group(2)).strip()

        anchor = slugify(title)

        toc.append(
            {
                "level": level,
                "title": title,
                "id": anchor,
            }
        )

        return f'<h{level} id="{escape(anchor)}">{match.group(2)}</h{level}>'

    updated_html = HEADING_PATTERN.sub(replace_heading, html)

    return updated_html, toc