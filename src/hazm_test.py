import hazm
import nlp

normal = nlp.normalizer_('میرم')
normal = nlp.informal_normalizer_(normal)

sentence_words = [ind2[0] for ind1 in normal for ind2 in ind1]
print(sentence_words)
sentence_words = [nlp.lemmatizer_(word) for word in sentence_words]
print(sentence_words)




