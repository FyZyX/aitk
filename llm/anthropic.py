import anthropic


class Claude:
    def __init__(self, api_key: str):
        self._client = anthropic.Client(api_key=api_key)

    @staticmethod
    def wrap_prompt(text):
        return f"{anthropic.HUMAN_PROMPT} {text}{anthropic.AI_PROMPT}"

    @staticmethod
    def token_count(content):
        return anthropic.count_tokens(content)

    def generate(self, prompt: str, max_tokens=200) -> str:
        return self._client.completion(
            prompt=self.wrap_prompt(prompt),
            stop_sequences=[anthropic.HUMAN_PROMPT],
            model="claude-v1-100k",
            max_tokens_to_sample=max_tokens,
        )["completion"]
