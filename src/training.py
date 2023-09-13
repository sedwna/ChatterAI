import random
import json
import pickle
import numpy as np
import nlp

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD


def trainer(json_name):
    print("pls wait until training completed...")
    json_file = open(f"../json_file/{json_name}.json", 'r',
                     encoding="utf8")
    intents = json.load(json_file)
    json_file.close()

    words = []
    classes = []
    documents = []

    for intent in intents['intents']:
        for pattern in intent["patterns"]:
            word_list = nlp.clean_up_sentence(pattern)
            words.extend(word_list)
            documents.append((word_list, intent["tag"]))
            if intent["tag"] not in classes:
                classes.append(intent['tag'])

    words = sorted(set(words))
    classes = sorted(set(classes))
    pickle.dump(words, open('../pkl_file/words.pkl', 'wb'))
    pickle.dump(classes, open('../pkl_file/classes.pkl', 'wb'))

    train_x = []
    train_y = []
    output_empty = [0] * len(classes)  # create zero array, count == number of tag in json file

    for document in documents:
        bag = []

        word_patterns = document[0]  # document[0] == word & document[1] == tag

        for word in words:
            # create a matrix by 0,1 value with all of words was in json file patterns
            bag.append(1) if word in word_patterns else bag.append(0)
        # set matrix tag
        output_row = list(output_empty)
        output_row[classes.index(document[1])] = 1

        # bag == 0,1 words matrix & output_row == 0,1 tags of words
        train_x.append(bag)
        train_y.append(output_row)

    train_x = np.array(train_x)  # feature
    train_y = np.array(train_y)  # label

    model = Sequential()
    model.add(Dense(128, input_shape=(len(train_x[0]),), activation="relu"))  # input layer
    model.add(Dropout(0.5))
    model.add(Dense(64, activation="relu"))  # hidden layer
    model.add(Dropout(0.5))
    model.add(Dense(len(train_y[0]), activation='softmax'))  # output layer

    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])
    print(np.array(train_x))
    print(np.array(train_y))
    hist = model.fit(np.array(train_x), np.array(train_y), epochs=50, batch_size=128, verbose=1)
    model.save('../chat_bot_model/chatbotmodel.h5', hist)

    print('your model is ready...\n'
          'to start chat with bot back to menu and choice option 10...')
    input("to continue press enter...")

    return
