import random
import json
import pickle
import numpy as np
import nlp

from tensorflow.keras.models import load_model


def bag_of_words(sentence, words):
    sentence_words = nlp.clean_up_sentence(sentence)
    print(sentence_words)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence, classes, model, words):
    bow = bag_of_words(sentence, words)
    print(bow)

    res = model.predict(np.array([bow]))[0]
    print(res)

    ERROR_THRESHOLD = 0.40
    results = [[i, r] for i, r in enumerate(res) ]  #if r > ERROR_THRESHOLD
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


def chatbot_model(json_name):
    intents = json.load(open(f"../json_file/{json_name}.json", 'r', encoding="utf8"))
    words = pickle.load(open('../pkl_file/words.pkl', 'rb'))
    classes = pickle.load(open('../pkl_file/classes.pkl', 'rb'))
    model = load_model('../chat_bot_model/chatbotmodel.h5')
    print(words)
    print("GO! Bot is running (enter -1 to exit)")
    message = input("you: ")
    while message != "-1":
        ints = predict_class(message, classes, model, words)
        if bool(ints):  # if bool == false, it means ints it's a empty and we dont have a response
            res = get_response(ints, intents)
            print("Bot: ", res)

        else:
            print("Bot: متاسفانه پاسخ مناسبی برای درخواست شما یافت نشد")
        print("-1 to exit")
        message = input("you: ")
    return
