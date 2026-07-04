import google.generativeai as genai

genai.configure(
    api_key="AIzaSyDnOydTwSJPYHthXUZVTeVSCUTZVnIjLYA"
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_answer(prompt):

    response = model.generate_content(
        prompt
    )

    return response.text