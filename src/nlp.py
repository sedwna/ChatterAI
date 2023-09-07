import hazm


def clean_up_sentence(sentence):
    sentence = normal(sentence)
    print("normalize: ",sentence)
    sentence_words = tokenize(sentence)
    sentence_words = [word for word in sentence_words]  # lemmatizer(word)

    return sentence_words


def stem(word):
    stemmer = hazm.Stemmer()
    return stemmer.stem(word)


def lemmatizer(word):
    return hazm.Lemmatizer().lemmatize(word)


def tokenize(sentence):
    return hazm.word_tokenize(sentence)


def normal(sentence):
    normalizer = hazm.Normalizer()

    return normalizer.normalize(sentence)
