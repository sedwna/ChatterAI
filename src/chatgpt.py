import openai

openai.api_key = "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"


def chatgpt(question):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                              messages=[{"role": "user", "content": f"{question} "}])
    return completion.choices[0].message.content
