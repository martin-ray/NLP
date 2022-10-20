# Import spaCy
import spacy

# need to download model first 
# by python3 -m spacy download en
# this produces lable for each word.
nlp = spacy.load("en_core_web_sm")



text = """Neil Alden Armstrong (5 August 1930 – 25 August 2012) was an American test pilot and astronaut, who was the commander of the Apollo 11 Moon landing mission on July 20, 1969,
 in which he and Buzz Aldrin were the first humans to land on the Moon, 
 and he was the first man to walk on the Moon."""
text_example = "I had many computers in my room , but my cat, Mike, broke all of them. "
doc = nlp(text) 
doc2 = nlp(text_example)

for token in doc:
    print(token.text, token.lemma_, token.pos_)

for token in doc2:
  print(token.text, token.lemma_)

# print PennTreeBank tags for each token (e.g., NN, NNS, VBZ...) 
# see https://spacy.io/usage/linguistic-features#pos-tagging

for token in doc:
    print(token.text, token.tag_) # fill in ??? and run this cell

for token in doc2:
    print(token.text, token.tag_)


# print Named Entity IOB-tags and tag-types for each token (e.g., PERSON, ORG, ...) 
# see https://spacy.io/usage/linguistic-features#named-entities and https://spacy.io/usage/linguistic-features#accessing-ner

for token in doc:
    print(token.text, token.ent_iob_, token.ent_type_) # fill in two ???s and run this cell.
  
for token in doc2:
    print(token.text, token.ent_iob_, token.ent_type_) # fill in two ???s and run this cell.

for token in doc.ents:
    print(token.text,  token.label_) # fill in two ???s and run this cell.

