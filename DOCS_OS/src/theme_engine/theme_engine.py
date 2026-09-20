from pathlib import Path
import json


class ThemeEngine:
    """
    DOCS_OS Theme Engine
    Loads typography and color tokens.
    """

    def __init__(self):
        self.root = Path(__file__).resolve().parents[2]
        self.theme_root = self.root / "01_THEMES"

        self.colors = self._load_json(
            self.theme_root / "colors" / "colors.json"
        )

        self.fonts = self._load_json(
            self.theme_root / "typography" / "fonts.json"
        )

    def _load_json(self, file_path: Path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def token(self, group, name):
        return self.colors[group][name]

    def font(self, section):
        return self.fonts[section]

    def export(self):
        return {
            "colors": self.colors,
            "fonts": self.fonts
        }


theme = ThemeEngine()