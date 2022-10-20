from collections import Counter

def extract_ngrams(text, N):
    ngrams = Counter()
    
    """ 
    e.g., 
    text = "the cat sat on the mat"    

    extract_ngrams(text, 1) must return
    {
      the: 2
      cats: 1
      sat: 1
      on: 1
      mat: 1
    }, 
    and extract_ngrams(text, 3) must return
    {
      the cats sat: 1
      cats sat on: 1
      sat on the: 1
      on the mat: 1
    }
 
    """
    tokens = text.split()
    for i in range(len(tokens)-N+1):
      ngram = " ".join(tokens[i:i+N])
      ngrams[ngram]+=1

    return ngrams


### This is an example usage of "extract_ngrams" function.
### You can see how it works. 

example_text = "the cats sat on the mat"

ngrams = extract_ngrams(example_text, 1)
print(ngrams)
ngrams = extract_ngrams(example_text, 2)
print(ngrams)
ngrams = extract_ngrams(example_text, 6)
print(ngrams)


text_from_wikipedia = """
Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data. 
The goal is a computer capable of "understanding" the contents of documents, including the contextual nuances of the language within them. The technology can then accurately extract information and insights contained in the documents as well as categorize and organize the documents themselves.
Challenges in natural language processing frequently involve speech recognition, natural-language understanding, and natural-language generation.
"""

print(extract_ngrams(text_from_wikipedia, 1))

print(extract_ngrams(text_from_wikipedia, 2))

print(extract_ngrams(text_from_wikipedia, 3))