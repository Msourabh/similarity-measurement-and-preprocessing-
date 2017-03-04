import math
import pickle
import glob
def jacaard(vec1,vec2):
    ls=vec1.keys()
    ls1=vec2.keys()
    intersection=len(set(ls)&set(ls1))
    union=len(set(ls)|set(ls1))
    if not union:
        return 0.0
    else:
        return float(intersection)/union
path='j:\mtech\others\irws code\data\*.pickle'
files=glob.glob(path)
for name in files:
    f=open(name,"rb")
    vec1=pickle.load(f)
    for name1 in files:
        if name1 is name:
            continue
        g=open(name1,"rb")
        vec2=pickle.load(g)
        jac=jacaard(vec1,vec2)
        print "similarity b/w   ",name,"and  ",name1,"is ",jac
        g.close()
    f.close()
