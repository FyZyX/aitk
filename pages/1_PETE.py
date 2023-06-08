import pathlib
import string

import streamlit as st
import yaml

CONFIG_PATH = pathlib.Path(__file__).parent / "prompts"
PROMPT_TEMPLATE_PATH = pathlib.Path(__file__).parent / "prompts/templates"


def load_config():
    with open(CONFIG_PATH / "config.yml") as file:
        return yaml.safe_load(file)


def load_prompt_template(name):
    with open(PROMPT_TEMPLATE_PATH / f"{name}.md") as file:
        return file.read()


def list_prompt_templates():
    return [x.stem for x in PROMPT_TEMPLATE_PATH.iterdir()]


def main():
    st.title(":blue[PETE]")
    st.header(':blue[P]rompt :blue[E]ngineering :blue[T]emplate :blue[E]ngine')

    templates = list_prompt_templates()
    name = st.selectbox("Select Template", options=templates)

    config = load_config()
    template_configs = config["templates"]
    template_config = template_configs[name]
    template_variables = template_config["variables"]

    template = load_prompt_template(name)
    template = st.text_area("Prompt", template)
    template = string.Template(template)
    identifiers = template.get_identifiers()
    values = {}
    for identifier in identifiers:
        if template_variables[identifier]["type"] == "string":
            value = st.text_input(identifier)
            values[identifier] = value

    rendered_template = template.substitute(**values)
    st.divider()
    st.markdown(rendered_template)


if __name__ == '__main__':
    main()
