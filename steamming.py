f=open("stem.txt")
from nltk.stem import PorterStemmer
for line in f:
    print line
    sing=[]
    stemmer=PorterStemmer()
    for p in line.split():
        sing.append(stemmer.stem(p))
        print "".join(sing)
