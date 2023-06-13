We need to translate HTML content into markdown. Read through the original content and then reproduce the same content using markdown syntax.

- Please remove any unnecessary structural markup, leave just the pertinent content.
- There should not be any remaining HTML syntax in your output.
- Remember that you must wrap all mathematical LaTeX notation with either one or two dollar signs for inline ($$ ... $$) or display mode ($$$$ ... $$$$) respectively:
- Avoid using LaTeX environments like `\begin{equation}`, in markdown, only the $$ syntax is valid
- Avoid splitting inline math expressions across multiple lines
- Avoid splitting lines in the middle of bold, emphasis, or code formatting
- Do not escape forward slashes in LaTeX expressions, meaning avoid `\\`
- Stick to the octothorpe (#) for headings H1 (#), H2 (##), H3 (###), etc.
- Pay special attention to whitespace, clean up excessive or extraneous whitespace and ensure line continuations avoid unnecessary indentation.
- Note that markdown images use the `[name](link)` syntax.

Your response should begin with the reformatted content directly, no additional prose.

ORIGINAL:
${lesson}