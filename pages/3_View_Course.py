import os
import pathlib

import streamlit as st

import llm.anthropic

API_KEY = os.environ.get("ANTHROPIC_API_KEY")


def concatenate_lessons(directory):
    with open('lessons/combined_lessons.md', 'w') as outfile:
        for chapter in range(1, 11):
            for section in range(1, 5):
                filename = f'lesson-{chapter}-{section}.md'
                filepath = directory / filename

                if filepath.is_file():
                    with open(filepath, 'r') as infile:
                        outfile.write(infile.read())
                    # Include a newline after each lesson for clarity
                    outfile.write('\n')
                else:
                    print(f"File {filepath} not found")


def main():
    st.title("Tutorial Maker")

    if st.button("Combine Files"):
        path = pathlib.Path("lessons/markdown")
        with st.spinner():
            concatenate_lessons(path)

    if st.button("Analyze"):
        model = llm.anthropic.Claude(API_KEY)
        with open('lessons/combined_lessons.md') as outfile:
            content = outfile.read()
        st.metric("Tokens", model.token_count(content))
        with st.spinner():
            response = model.generate(content, max_tokens=20_000)
        st.markdown(response)
        with open("lessons/ftc.md", "w") as file:
            file.write(response)


if __name__ == '__main__':
    main()
