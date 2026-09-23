import re
from html import unescape

# ==========================================================
# DOCS_OS TOC Builder v1.1
# ==========================================================

HEADING_PATTERN = re.compile(
    r"<h([23])(?:\s+id=[\"']([^\"']+)[\"'])?>(.*?)</h\1>",
    re.IGNORECASE | re.DOTALL,
)


def strip_html(text: str) -> str:
    """Remove HTML tags and decode HTML entities from heading text."""
    text = re.sub(r"<[^>]+>", "", text)
    return unescape(text).strip()


def slugify(text: str) -> str:
    """
    Convert heading text into a stable URL-friendly anchor.

    Example:
        Chapter 1 — Documentation Philosophy
        -> chapter-1-documentation-philosophy
    """

    text = strip_html(text).lower()

    # Normalize common dash characters.
    text = re.sub(r"[—–−]", "-", text)

    # Keep only letters, numbers, spaces and dashes.
    text = re.sub(r"[^a-z0-9\s-]", "", text)

    # Convert whitespace runs into single dashes.
    text = re.sub(r"\s+", "-", text)

    # Collapse repeated dashes.
    text = re.sub(r"-+", "-", text)

    return text.strip("-")


def build_toc(html: str):
    """
    Add stable IDs to H2/H3 headings and return TOC metadata.

    Returns:
        (
            updated_html,
            [
                {
                    "level": 2,
                    "title": "...",
                    "id": "..."
                },
                ...
            ]
        )
    """

    toc = []
    used_ids = set()

    def replace_heading(match):
        level = int(match.group(1))
        existing_id = match.group(2)
        inner_html = match.group(3)

        title = strip_html(inner_html)

        # Prefer an existing ID when one was already provided.
        base_id = existing_id or slugify(title)

        # Guarantee a usable fallback.
        if not base_id:
            base_id = f"section-{len(toc) + 1}"

        # Guarantee uniqueness.
        anchor = base_id
        counter = 2

        while anchor in used_ids:
            anchor = f"{base_id}-{counter}"
            counter += 1

        used_ids.add(anchor)

        toc.append(
            {
                "level": level,
                "title": title,
                "id": anchor,
            }
        )

        return f'<h{level} id="{anchor}">{inner_html}</h{level}>'

    updated_html = HEADING_PATTERN.sub(replace_heading, html)

    return updated_html, toc