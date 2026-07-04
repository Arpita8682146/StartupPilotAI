from prompt_builder import build_prompt

question = "How can startups get funding?"

context = """
Government funding schemes are available.
Startup India supports innovation.
"""

prompt = build_prompt(
    question,
    context
)

print(prompt)