
import json
import pickle
import numpy as np
import nlp


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout, LSTM, Input, Embedding
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.sequence import pad_sequences


def trainer_bag_of_word(json_name):
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
    pickle.dump(words, open(f'../pkl_file/{json_name}_words.pkl', 'wb'))
    pickle.dump(classes, open(f'../pkl_file/{json_name}_classes.pkl', 'wb'))

    train_x = []
    train_y = []
    # create zero array, count == number of tag in json file
    output_empty = [0] * len(classes)

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
    # input layer
    model.add(Dense(128, input_shape=(len(train_x[0]),), activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation="relu"))  # hidden layer
    model.add(Dropout(0.5))
    model.add(Dense(len(train_y[0]), activation='softmax'))  # output layer

    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

    model.compile(optimizer=sgd, loss='categorical_crossentropy', metrics=['accuracy'])
    hist = model.fit(np.array(train_x), np.array(train_y), epochs=50, batch_size=128, verbose=1)
    model.save('../chat_bot_model/chatbotmodel.h5', hist)

    model.compile(optimizer=sgd, loss='categorical_crossentropy',
                  metrics=['accuracy'])
    print(np.array(train_x))
    print(np.array(train_y))
    hist = model.fit(np.array(train_x), np.array(train_y),
                     epochs=50, batch_size=128, verbose=1)
    model.save(f'../chat_bot_model/{json_name}_model.h5', hist)


    print('your model is ready...\n'
          'to start chat with bot back to menu and choice option 10...')
    input("to continue press enter...")

    return


def trainer_weight(json_name):
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
    pickle.dump(words, open(f'../pkl_file/{json_name}_words.pkl', 'wb'))
    pickle.dump(classes, open(f'../pkl_file/{json_name}_classes.pkl', 'wb'))

    max_words = len(words)
    tkn = Tokenizer(num_words=max_words)
    tkn.fit_on_texts(intent[0] for intent in documents)
    with open(f'../pkl_file/{json_name}_tkn.pkl', 'wb') as handle:
        pickle.dump(tkn, handle, protocol=pickle.HIGHEST_PROTOCOL)
    seq = tkn.texts_to_sequences(intent[0] for intent in documents)

    train_y = [intent[1] for intent in documents]

    d = dict(zip(classes, range(0, len(classes))))
    train_y = [[d[word]] for word in train_y]
    train_y = list(train_y)
    train_y = np.array(train_y)

    train_y = to_categorical(train_y, len(classes))
    max_len = 20
    paded_docs = pad_sequences(seq, maxlen=max_len, padding="pre")
    print(paded_docs)
    embedding_vector_features = 30
    model = Sequential()
    model.add(Embedding(max_words, embedding_vector_features, input_length=max_len))
    model.add(LSTM(256))
    model.add(Dense(len(train_y[0]), activation='softmax'))
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy', metrics=['accuracy'])
    hist = model.fit(np.array(paded_docs), np.array(
        train_y), batch_size=128, epochs=25)
    model.save(f'../chat_bot_model/{json_name}_model.h5', hist)
    print('your model is ready...\n'
          'to start chat with bot back to menu and choice option 10...')
    input("to continue press enter...")

    return
