import typing

import anthropic


class Claude:
    def __init__(self, api_key: str):
        self._client = anthropic.Anthropic(api_key=api_key)

    def wrap_prompt(self, text):
        return f"{self._client.HUMAN_PROMPT} {text}{self._client.AI_PROMPT}"

    def token_count(self, content):
        return self._client.count_tokens(content)

    def generate(self, prompt: str, max_tokens=200):
        yield from self._client.completions.create(
            prompt=self.wrap_prompt(prompt),
            stop_sequences=[anthropic.HUMAN_PROMPT],
            model="claude-2",
            max_tokens_to_sample=max_tokens,
            stream=True,
        )
