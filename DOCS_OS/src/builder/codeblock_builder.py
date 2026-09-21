import re

LANGS = [
    "python",
    "sql",
    "json",
    "yaml",
    "bash",
    "text",
    "js",
    "ts",
    "tsx",
]

def replace_codeblocks(html: str) -> str:

    pattern = re.compile(
        r'<pre><code class="language-(.*?)">(.*?)</code></pre>',
        re.DOTALL,
    )

    def repl(match):

        lang = match.group(1).upper()
        code = match.group(2)

        return f"""
<div class="codeblock">

    <div class="codeblock-toolbar">

        <div class="codeblock-language">{lang}</div>

        <button class="copy-button">Copy</button>

    </div>

    <pre><code>{code}</code></pre>

</div>
"""

    return pattern.sub(repl, html)