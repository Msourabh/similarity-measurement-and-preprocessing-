import re, math
from collections import Counter
WORD = re.compile(r'\w+')
def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

text1 = "This ,is ==a foo -bar , sentence ."
text2 = 'This sentence is similar to a foo bar sentence .'

vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)
print vector1
