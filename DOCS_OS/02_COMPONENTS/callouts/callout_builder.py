import re

ICONS = {
    "INFO": "i",
    "SUCCESS": "✓",
    "WARNING": "!",
    "DANGER": "−",
}

def replace_callouts(html: str) -> str:
    """
    Converts every blockquote containing
    [INFO] [WARNING] [SUCCESS] [DANGER]
    into an individual callout card.
    """

    pattern = re.compile(
        r"<blockquote>\s*<p>\[(INFO|SUCCESS|WARNING|DANGER)\]\s*(.*?)</p>\s*</blockquote>",
        re.DOTALL,
    )

    def repl(match):
        kind = match.group(1)
        message = match.group(2).strip()
        icon = ICONS[kind]

        return f"""
<div class="callout {kind.lower()}">
    <div class="callout-header">
        <span class="callout-icon">{icon}</span>
        <span class="callout-title">{kind}</span>
    </div>

    <div class="callout-body">
        {message}
    </div>
</div>
"""

    return pattern.sub(repl, html)