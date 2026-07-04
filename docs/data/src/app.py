from retriever import retrieve_context
from prompt_builder import build_prompt
from gemini_client import generate_answer

print("Program started")

question = input("Ask: ")

print(question)

from rag_pipeline import ask


print(

"Program Started"

)

while True:

    question = input(

        "\nAsk: "

    )

    if question.lower()=="exit":

        break

    answer = ask(

        question

    )

    print(

        "\nAnswer:\n"

    )

    print(

        answer

    )