from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

THEMES = {
    "apple_dark": ROOT / "01_THEMES" / "apple_dark" / "theme.css"
}


def load_theme(theme_name="apple_dark"):
    """
    Load CSS theme as a string.
    """

    if theme_name not in THEMES:
        raise ValueError(f"Unknown theme: {theme_name}")

    css_file = THEMES[theme_name]

    if not css_file.exists():
        raise FileNotFoundError(f"Theme not found: {css_file}")

    return css_file.read_text(encoding="utf-8")