import hazm


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
