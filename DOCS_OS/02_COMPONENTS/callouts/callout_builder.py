import re

ICONS = {
    "INFO": "i",
    "SUCCESS": "✓",
    "WARNING": "!",
    "DANGER": "−"
}


def replace_callouts(html: str) -> str:
    pattern = re.compile(
        r'<blockquote>\s*<p>\[(INFO|SUCCESS|WARNING|DANGER)\]\s*(.*?)</p>\s*</blockquote>',
        re.DOTALL
    )

    def repl(match):
        callout_type = match.group(1)
        message = match.group(2).strip()
        icon = ICONS[callout_type]

        return f"""
<div class="callout {callout_type.lower()}">

    <div class="callout-header">
        <div class="callout-icon">{icon}</div>
        <div class="callout-title">{callout_type}</div>
    </div>

    <div class="callout-body">{message}</div>

</div>
"""

    return pattern.sub(repl, html)