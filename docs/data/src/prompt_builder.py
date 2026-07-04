def build_prompt(

question,

context

):

    prompt = f"""

You are StartupPilotAI.

Use the information below.

Context:

{context}

Question:

{question}

Provide an answer.

"""

    return prompt