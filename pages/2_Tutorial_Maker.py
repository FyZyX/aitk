import os

import bs4
import streamlit as st

import llm.anthropic
import llm.prompt

API_KEY = os.environ.get("ANTHROPIC_API_KEY")


class LessonFormatter:

    def __init__(self, chapter: int, lesson: int,
                 model: llm.anthropic.Claude,
                 template: llm.prompt.PromptTemplate):
        self._chapter = chapter
        self._lesson = lesson
        self._model = model
        self._template = template
        self._blocks = None
        self._formatted_blocks = None

    def _load_lesson_blocks(self):
        path = f"lessons/lesson-{self._chapter}-{self._lesson}.html"
        with open(path) as file:
            content = bs4.BeautifulSoup(file.read(), 'html.parser')
        return content.find_all("safe-richtext")

    def _reformat_block(self, lesson):
        prompt = self._template.render(lesson=lesson)
        token_limit = self._model.token_count(lesson) + 150
        return self._model.generate(
            prompt=prompt,
            max_tokens=token_limit,
        )

    def _reformat_blocks(self):
        if not self._blocks:
            self._load_lesson_blocks()
        yield from map(self._reformat_block, self._blocks)

    def reformat_lesson(self):
        if not self._formatted_blocks:
            for block in self._reformat_blocks():
                self._formatted_blocks.append(block)
                yield block
        return "\n\n".join(self._formatted_blocks)


def main():
    st.title("Tutorial Maker")

    model = llm.anthropic.Claude(api_key=API_KEY)
    prompt_template = llm.prompt.PromptTemplate("alg-calc-html-converter")
    lesson_formatter = LessonFormatter(1, 1, model, prompt_template)

    if st.button("Reformat Lesson"):
        with st.spinner():
            lesson = lesson_formatter.reformat_lesson()
            for block in lesson:
                st.markdown(block)
        st.session_state["lesson"] = lesson

    lesson = st.session_state.get("lesson")
    st.code(lesson)


if __name__ == '__main__':
    main()
