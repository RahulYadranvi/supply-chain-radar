import re
import html


def replace_codeblocks(html_content):
    """
    Converts Python-Markdown generated code blocks

    <pre><code class="language-python">...</code></pre>

    into DOCS_OS premium Apple code blocks.
    """

    pattern = re.compile(
        r'<pre><code(?: class="language-([^"]+)")?>(.*?)</code></pre>',
        re.DOTALL,
    )

    def build(match):
        language = match.group(1) or "TEXT"

        code = html.unescape(match.group(2))

        code = code.replace("\r\n", "\n").strip("\n")

        escaped = html.escape(code)

        return f"""
<div class="codeblock">

    <div class="codeblock-toolbar">

        <span class="codeblock-language">{language.upper()}</span>

        <button class="copy-button">Copy</button>

    </div>

    <pre><code>{escaped}</code></pre>

</div>
"""

    return pattern.sub(build, html_content)