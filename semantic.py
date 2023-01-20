import spacy

#==========ADVANCED LANGUAGE MODEL===============#

nlp = spacy.load("en_core_web_md")  # load spacy library

#  variables that will be compared.
tokens = nlp ("cat monkey banana")

# display results.
for token1 in tokens:
    for token2 in tokens:
        print(f"{token1.text:^6s} x {token2.text:^6s} - similarity: {round(token1.similarity(token2), 2)}.")

'''It is interesting to know how the words cat and monkey seem to be similar - probably - due to the fact that both are animals
and that banana have a higher similarity rather than banana and cat. Probably due to mith of that monkeys only eat banana.'''



#==========SIMPLE LANGUAGE MODEL===============#

nlp2 = spacy.load("en_core_web_sm")  # load spacy library

#  variables that will be compared.
tokens = nlp2 ("cat monkey banana")

# display results.
for token1 in tokens:
    for token2 in tokens:
        print(f"{token1.text:^6s} x {token2.text:^6s} - similarity: {round(token1.similarity(token2), 2)}.")

'''Very interesting result! Apparently, I received a Warning Message:
UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Token.similarity method will be 
based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the 
small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add 
your own word vectors, or use one of the larger models instead if available.

It is not like didn't work, but gave me completelly different numbers. So, apparently it gives you a non-trustful values which is,
in the end, useless.
'''

