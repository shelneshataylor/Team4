

import openai


openai.api_key = "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"


def chat_with_gpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
        )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)