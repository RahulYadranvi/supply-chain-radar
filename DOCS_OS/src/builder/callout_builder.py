import re

ICONS = {
    "INFO": "ⓘ",
    "SUCCESS": "✓",
    "WARNING": "▲",
    "DANGER": "●",
}


def replace_callouts(html: str) -> str:
    """
    Convert markdown blockquotes into individual callout cards.
    Works with Python-Markdown output, where consecutive '>' lines become
    one <blockquote> with multiple <p> elements.
    """

    blockquote_pattern = re.compile(
        r"<blockquote>(.*?)</blockquote>",
        re.DOTALL,
    )

    paragraph_pattern = re.compile(
        r"<p>\[(INFO|SUCCESS|WARNING|DANGER)\]\s*(.*?)</p>",
        re.DOTALL,
    )

    def convert_blockquote(match):
        block_content = match.group(1)

        callouts = paragraph_pattern.findall(block_content)

        # Normal blockquote → leave unchanged.
        if not callouts:
            return match.group(0)

        html_cards = []

        for kind, message in callouts:
            html_cards.append(f"""
<div class="callout {kind.lower()}">
    <div class="callout-header">
        <span class="callout-icon">{ICONS[kind]}</span>
        <span class="callout-title">{kind}</span>
    </div>
    <div class="callout-body">{message.strip()}</div>
</div>
""")

        return "\n".join(html_cards)

    return blockquote_pattern.sub(convert_blockquote, html)