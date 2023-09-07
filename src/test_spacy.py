import spacy
from spacy.lang.fa import stop_words

nlp = stop_words()

# nlp_fa = spacy.blank("fa")

print(nlp("فرماندهان"))