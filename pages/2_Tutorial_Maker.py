import functools
import os

import bs4
import streamlit as st

import llm.anthropic
import llm.prompt

API_KEY = os.environ.get("ANTHROPIC_API_KEY")


def get_lesson_blocks():
    with open("lessons/lesson-1-1.html") as file:
        content = file.read()
    parsed_content = bs4.BeautifulSoup(content, 'html.parser')
    content_blocks = parsed_content.find_all("safe-richtext")
    return content_blocks


def reformat_block(model, lesson):
    prompt = llm.prompt.PromptTemplate("alg-calc-html-converter")
    token_limit = llm.anthropic.token_count(lesson) + 150
    return model.generate(
        prompt=prompt.render(lesson=lesson),
        max_tokens=token_limit,
    )


def reformat_blocks(model, blocks):
    f = functools.partial(reformat_block, model)
    yield from map(f, blocks)


def main():
    st.title("Tutorial Maker")

    model = llm.anthropic.Claude(api_key=API_KEY)
    blocks = get_lesson_blocks()
    if st.button("Reformat Lesson"):
        formatted_blocks = []
        with st.spinner():
            for block in reformat_blocks(model, blocks):
                st.markdown(block)
                formatted_blocks.append(block)

        st.session_state["lesson"] = "\n\n".join(formatted_blocks)
    lesson = st.session_state.get("lesson")
    st.code(lesson)


if __name__ == '__main__':
    main()
