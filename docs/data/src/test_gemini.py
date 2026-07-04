from gemini_client import generate_answer

prompt = """
You are StartupPilotAI.

Context:

Government funding schemes are available.
Startup India supports innovation.

Question:

How can startups get funding?

Provide an answer.
"""

answer = generate_answer(
    prompt
)

print(answer)