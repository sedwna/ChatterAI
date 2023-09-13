import hazm

# wordEmbedding = hazm.WordEmbedding(model_type='fasttext')
# wordEmbedding.load_model('fasttext_skipgram_300.bin')
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Activation, Dense, Dropout, Input, Embedding

import pandas as pd
import numpy as np
import json
import nlp

print("pls wait until training completed...")
json_file = open(f"../json_file/intents.json", 'r',
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

max_words = len(words)
tkn = Tokenizer(num_words=max_words)
tkn.fit_on_texts(intent[0] for intent in documents)
seq = tkn.texts_to_sequences(intent[0] for intent in documents)
train_y = [intent[1] for intent in documents]

d = dict(zip(classes, range(0, len(classes))))
train_y = [[d[word]] for word in train_y]
train_y = list(train_y)

train_y = np.array(train_y)

max_len = 20
paded_docs = pad_sequences(seq, maxlen=max_len, padding="pre")

embedding_vector_features = 30
model = Sequential()
model.add(Embedding(max_words, embedding_vector_features, input_length=max_len))
model.add(LSTM(256))
model.add(Dense(len(classes), activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy',
              metrics=['accuracy'])
model.summary()
print(np.array(paded_docs))
print(np.array(train_y))
hist = model.fit(np.array(paded_docs), np.array(train_y), epochs=50, batch_size=128, verbose=1)
# model.fit(paded_docs, train_y, batch_size=128, epochs=10)
