import hazm


def clean_up_sentence(sentence):
    sentence_words = tokenize(sentence)
    sentence_words = [word for word in sentence_words]  # lemmatizer(word)

    return sentence_words


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
