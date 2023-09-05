import random
import json
import pickle
import numpy as np
import hazm

from tensorflow.keras.models import load_model


def lemmatizer(word):
    return hazm.Lemmatizer().lemmatize(word)


def tokenize(sentence):
    return hazm.word_tokenize(sentence)


intents = json.load(open("../json_file/info.json", 'r', encoding="utf8"))
words = pickle.load(open('../pkl_file/words.pkl', 'rb'))
classes = pickle.load(open('../pkl_file/classes.pkl', 'rb'))
model = load_model('../AI_conversation_creator/chat_bot_model/chatbotmodel.h5')
print(model.predict)
print(words)
print(len(words))


def clean_up_sentence(sentence):
    sentence_words = tokenize(sentence)
    sentence_words = [word for word in sentence_words]  # lemmatizer(word)

    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    print(sentence_words)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    print(bow)

    res = model.predict(np.array([bow]))[0]
    print(res)

    ERROR_THRESHOLD = 0.27
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]  #
    results.sort(key=lambda x: x[1], reverse=True)
    print(results)

    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    print("return list", return_list)

    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


print("GO! Bot is running")
message = input("you: ")
while message != "خروج":
    ints = predict_class(message)
    if bool(ints):
        res = get_response(ints, intents)
        print("Bot: ", res)

    else:
        print("Bot: we cant find a answer")

    message = input("")
