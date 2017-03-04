import math
import sys
import glob
import errno
import pickle
def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator
#print "hwllo"
path='J:\mtech\others\irws code\data\*.pickle'
#print "hwllo"
files=glob.glob(path)
#print "hwllo"
for name in files:
    #print "hwllo"
    f=open(name,"rb")
    vec1=pickle.load(f)
    for name1 in files:
        if name1 is name:
            continue
        print "similarity between",name,name1,"is" 
        g=open(name1,"rb")
        #print "hwllo"
        vec2=pickle.load(g)
        cosine=get_cosine(vec1,vec2)
        print "cosine is ",cosine
        g.close()
    f.close()

                    
