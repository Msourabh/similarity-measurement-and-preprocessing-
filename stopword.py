from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
example="this is an example showing off stop word filtration."
stop_word=set(stopwords.words("english"))
words=word_tokenize(example)
fil=[]
for w in words:
    if w not in stop_word:
        fil.append(w)

print (fil)

        
