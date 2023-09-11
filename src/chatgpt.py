import openai

openai.api_key = "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"


def chatgpt(question):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                              messages=[{"role": "user", "content": f"{question} "}])
    return completion.choices[0].message.content
