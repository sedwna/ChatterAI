import hazm


def clean_up_sentence(sentence):
    ignore_letters = ['?', '!', ',', '.', '؟؟', '!!', '!!!', '؟؟؟','؟']
    sentence = normalizer_(sentence)
    sentence_words = informal_normalizer_(sentence)  # informal and tokenize
    sentence_words = [ind2[0] for ind1 in sentence_words for ind2 in ind1]  # if 2 index just get first word
    sentence_words = [lemmatizer_(word) for word in sentence_words if word not in ignore_letters]
    # print("normalize: ", sentence_words)

    return sentence_words


# -------------------------------------------------------------------------------

def stemmer_(word):  # not use
    stemmer = hazm.Stemmer()
    return stemmer.stem(word)


# -------------------------------------------------------------------------------


def lemmatizer_(word):
    return hazm.Lemmatizer().lemmatize(word)


# -------------------------------------------------------------------------------

def tokenizer_(sentence):
    return hazm.word_tokenize(sentence)


# -------------------------------------------------------------------------------

def normalizer_(sentence):
    normalizer = hazm.Normalizer()

    return normalizer.normalize(sentence)


# -------------------------------------------------------------------------------

def informal_normalizer_(sentence):
    normalizer = hazm.InformalNormalizer()
    return normalizer.normalize(sentence)
# -------------------------------------------------------------------------------
def sentence_tokenizer(sentence):
    tokenizer = hazm.SentenceTokenizer()
    return tokenizer.tokenize(sentence)