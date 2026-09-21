import re

CALLOUTS = {
    "INFO": ("info", "ℹ️"),
    "WARNING": ("warning", "⚠️"),
    "SUCCESS": ("success", "✔️"),
    "DANGER": ("danger", "⛔"),
}


def replace_callouts(html: str):
    """
    Converts every paragraph starting with [INFO], [WARNING], etc.
    into an Apple-style callout card.
    Works whether the markdown parser wraps them in one blockquote
    or separate blockquotes.
    """

    # Remove blockquote wrappers first
    html = html.replace("<blockquote>", "").replace("</blockquote>", "")

    for label, (css_class, icon) in CALLOUTS.items():
        pattern = rf"<p>\s*\[{label}\]\s*(.*?)</p>"

        def repl(match):
            text = match.group(1).strip()

            return f"""
<div class="callout {css_class}">
    <div class="callout-icon">{icon}</div>
    <div class="callout-content">
        <h4>{label}</h4>
        <p>{text}</p>
    </div>
</div>
"""

        html = re.sub(pattern, repl, html, flags=re.DOTALL)

    return html