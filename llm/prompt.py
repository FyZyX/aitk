import pathlib
import string

import yaml


class Prompt:
    _config_root = pathlib.Path(__file__).parent / "prompts"
    _prompt_template_path = _config_root / "templates"

    def __init__(self, name):
        self._name = name
        self._template: string.Template | None = None

    @classmethod
    def load_config(cls):
        with open(cls._config_root / "config.yml") as file:
            return yaml.safe_load(file)

    def _path(self):
        return self._prompt_template_path / f"{self._name}.md"

    def load_template(self):
        with open(self._path()) as file:
            self._template = string.Template(file.read())

    def render(self, **variables):
        if not self._template:
            self.load_template()
        return self._template.substitute(**variables)
