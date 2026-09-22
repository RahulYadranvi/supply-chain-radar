"""
==========================================================
DOCS_OS Code Block Builder
Version : v0.3.1-alpha
Converts Markdown fenced code blocks into Apple-style blocks.
==========================================================
"""

import html
import re


def replace_codeblocks(content: str) -> str:
    """
    Converts:

    ```python
    print("Hello")
    ```

    into:

    <div class="codeblock">
        ...
    </div>
    """

    pattern = re.compile(r"```(\w+)?\n(.*?)```", re.DOTALL)

    def render(match):
        language = (match.group(1) or "TEXT").upper()
        code = match.group(2).rstrip()

        # Escape HTML characters so code displays correctly.
        escaped_code = html.escape(code, quote=False)

        return f"""
<div class="codeblock">

    <div class="codeblock-toolbar">

        <span class="codeblock-language">{language}</span>

        <button class="copy-button">Copy</button>

    </div>

    <pre><code>{escaped_code}</code></pre>

</div>
"""

    return pattern.sub(render, content)