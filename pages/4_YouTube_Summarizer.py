import os
from urllib.parse import urlparse, parse_qs

import streamlit
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

import llm.anthropic
import llm.prompt

API_KEY = os.environ.get("ANTHROPIC_API_KEY")


def get_video_id(url) -> str:
    parsed_url = urlparse(url)
    query_parameters = parse_qs(parsed_url.query)

    video_id = query_parameters.get("v", None)

    if video_id:
        return video_id[0]
    else:
        raise ValueError("Video ID not found in URL")


def main():
    st.title("YouTube Transcript")

    url = streamlit.text_input("Video URL")
    if not url:
        return
    video_id = get_video_id(url)
    streamlit.code(video_id)

    if streamlit.button("Run"):
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        # streamlit.json(transcript)
        text = " ".join([item["text"] for item in transcript])

        claude = llm.anthropic.Claude(API_KEY)
        prompt = f"""\
Based on the provided transcript of a video from Normal Wildberger's Algebraic Calculus course, please summarize the content with a particular focus on the following aspects:

1. **Main Concepts:** Detail the core ideas, principles, and theories discussed. Identify any new or unique approaches that Wildberger introduces, and explain how they relate to or differ from traditional calculus concepts.
2. **Logical Structure:** Break down the content into logical sections, and provide an ordered sequence of the topics covered. This includes definitions, theorems, proofs, and examples, as well as any connections between them.
3. **Visual Connections:** Suggest a conceptual diagram or a set of diagrams that could represent the topics discussed. Describe the elements, relationships, and structures that could be illustrated, and how they would help in understanding the material.
4. **Mathematical Insights:** Extract and explain mathematical formulas, equations, or expressions used in the video. Analyze the role they play in the overall conceptual framework of algebraic calculus according to Wildberger.
5. **Critical Analysis:** Provide an analysis of Wildberger's approach to calculus. How does it fit within the broader context of mathematical education? Are there any controversial or unconventional methods that warrant further exploration?
6. **Questions and Reflection:** Pose a set of questions that encourage deeper reflection on the material, targeting understanding, application, analysis, and synthesis. These questions should be designed for learners seeking to grasp the full breadth and depth of the subject.

Please ensure that the summary retains the nuance and intricacy of the content, offering a comprehensive view that can be used for educational and analytical purposes.

TRANSCRIPT
---
{text}
"""
        summary = claude.stream(prompt, max_tokens=25_000)
        completion_text = ""
        text_area = st.empty()

        for completion in summary:
            token_text = completion.completion
            completion_text += token_text
            text_area.markdown(completion_text)


if __name__ == '__main__':
    main()
