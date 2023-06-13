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
        self._blocks = []
        self._formatted_blocks = []

    def __len__(self):
        if not self._blocks:
            self._load_lesson_blocks()
        return len(self._blocks)

    def _load_lesson_blocks(self):
        path = f"lessons/lesson-{self._chapter}-{self._lesson}.html"
        with open(path) as file:
            content = bs4.BeautifulSoup(file.read(), 'html.parser')
        self._blocks = content.find_all("safe-richtext")

    def _reformat_block(self, lesson):
        lesson = str(lesson)
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

    def process_blocks(self):
        if not self._formatted_blocks:
            for block in self._reformat_blocks():
                self._formatted_blocks.append(block)
                yield block
        else:
            yield from self._formatted_blocks

    def result(self):
        return "\n\n".join(self._formatted_blocks)

    def save(self):
        path = f"lessons/formatted/lesson-{self._chapter}-{self._lesson}.md"
        result = self.result()
        with open(path, "w") as file:
            file.write(result)
        return result


def main():
    st.title("Tutorial Maker")

    model = llm.anthropic.Claude(api_key=API_KEY)
    prompt_template = llm.prompt.PromptTemplate("alg-calc-html-converter")
    cols = st.columns(2)
    with cols[0]:
        chapter = st.number_input("Chapter", min_value=1, max_value=10, step=1)
    with cols[1]:
        lesson_number = st.number_input("Lesson", min_value=1, max_value=4, step=1)
    lesson_formatter = LessonFormatter(chapter, lesson_number, model, prompt_template)

    if st.button("Reformat Lesson"):
        progress_text = "Formatting lesson. Please wait."
        progress_bar = st.progress(0, text=progress_text)
        with st.spinner():
            n = len(lesson_formatter)
            for i, block in enumerate(lesson_formatter.process_blocks()):
                st.markdown(block)
                progress_bar.progress((i + 1) / n, text=progress_text)
        result = lesson_formatter.save()
        st.session_state["lesson"] = result

    lesson = st.session_state.get("lesson", "")
    st.code(lesson)


if __name__ == '__main__':
    main()
