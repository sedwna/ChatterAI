import random
import json
import pickle
import numpy as np
import hazm

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

stemmer = hazm.Stemmer()


def stem(word):
    return stemmer.stem(word)


def lemmatizer(word):
    return hazm.Lemmatizer().lemmatize(word)


def tokenize(sentence):
    return hazm.word_tokenize(sentence)


def normal(sentence):
    normalizer = hazm.Normalizer()

    return normalizer.normalize(sentence)


intents = json.load(open("../json_file/info.json", 'r', encoding="utf8"))

words = []
classes = []
documents = []
ignore_letters = ['?', '!', ',', '.', '؟']

for intent in intents['intents']:
    for pattern in intent["patterns"]:
        pattern = normal(pattern)
        word_list = tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent["tag"]))
        if intent["tag"] not in classes:
            classes.append(intent['tag'])

words = [word for word in words if word not in ignore_letters]  # lemmatizer(word)

print(words)
print(len(words))
print(classes)
print(len(classes))

words = sorted(set(words))
classes = sorted(set(classes))
pickle.dump(words, open('../pkl_file/words.pkl', 'wb'))
pickle.dump(classes, open('../pkl_file/classes.pkl', 'wb'))
# print(words)

training = []
output_empty = [0] * len(classes)

print(output_empty)
print(documents)

for document in documents:
    bag = []

    word_patterns = document[0]
    # word_patterns = [word for word in words if word not in ignore_letters]  # lemmatizer(word)
    # print(word_patterns)
    # print(len(word_patterns))
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])
print(training)
print("-----------------------")
random.shuffle(training)
print(training)
training = np.array(training)

train_x = list(training[:, 0])
train_y = list(training[:, 1])

print(train_x)
print(train_y)
print(len(train_x))
print(len(train_y))

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=50, batch_size=128, verbose=1)
model.save('../chat_bot_model/chatbotmodel.h5', hist)
print('Done')
