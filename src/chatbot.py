import random
import json
import pickle
import numpy as np
import nlp
import chatgpt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


def bag_of_words(sentence, words):
    sentence_words = nlp.clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def bag_predict_class(sentence, classes, model, words):
    bow = bag_of_words(sentence, words)
    # print(bow)

    res = model.predict(np.array([bow]))[0]
    # print(res)

    ERROR_THRESHOLD = 0.20
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    # print(results)

    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    # print("return list", return_list)

    return return_list


def weight_predict_class(model, test_paded, classes):

    res = model.predict(np.array(test_paded))[0]
    ERROR_THRESHOLD = 0.20
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)

    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    print(return_list)
    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


def bag_chatbot_model(json_name):
    intents = json.load(open(f"../json_file/{json_name}.json", 'r', encoding="utf8"))
    words = pickle.load(open(f'../pkl_file/{json_name}_words.pkl', 'rb'))
    classes = pickle.load(open(f'../pkl_file/{json_name}_classes.pkl', 'rb'))
    model = load_model(f'../chat_bot_model/{json_name}_model.h5')
    # print(words)
    print("GO! Bot is running (enter -1 to exit)")
    messages = input("you: ")
    while messages != "-1":
        messages = nlp.sentence_tokenizer(messages)
        for message in messages:
            ints = bag_predict_class(message, classes, model, words)
            if bool(ints):  # if bool == false, it means ints it's a empty and we don`t have a response
                res = get_response(ints, intents)
                print("Bot: ", res)

            else:
                try:
                    res = chatgpt.chatgpt(message)
                    print("Bot: ", res)
                except:
                    print("Bot: متاسفانه پاسخ مناسبی برای درخواست شما یافت نشد")
        print("-1 to exit")
        messages = input("you: ")
    return


def weight_chatbot_model(json_name):
    intents = json.load(open(f"../json_file/{json_name}.json", 'r', encoding="utf8"))
    words = pickle.load(open(f'../pkl_file/{json_name}_words.pkl', 'rb'))
    classes = pickle.load(open(f'../pkl_file/{json_name}_classes.pkl', 'rb'))
    model = load_model(f'../chat_bot_model/{json_name}_model.h5')
    max_words = len(words)
    with open(f'../pkl_file/{json_name}_tkn.pkl', 'rb') as handle:
        tkn = pickle.load(handle)

    max_len = 20
    # print(words)
    print("GO! Bot is running (enter -1 to exit)")
    messages = input("you: ")
    while messages != "-1":

        messages = nlp.sentence_tokenizer(messages)
        for message in messages:
            print(message)
            message = nlp.clean_up_sentence(message)
            message = " ".join(message)
            print(message)

            test_seq = tkn.texts_to_sequences([message])
            print(test_seq)
            test_paded = pad_sequences(test_seq, maxlen=max_len, padding="pre")
            print(test_paded)
            ints = weight_predict_class(model, test_paded, classes)

            if bool(ints):  # if bool == false, it means ints it's a empty and we don`t have a response
                res = get_response(ints, intents)
                print("Bot: ", res)

            else:
                try:
                    res = chatgpt.chatgpt(message)
                    print("Bot: ", res)
                except:
                    print("Bot: متاسفانه پاسخ مناسبی برای درخواست شما یافت نشد")
        print("-1 to exit")
        messages = input("you: ")
    return
