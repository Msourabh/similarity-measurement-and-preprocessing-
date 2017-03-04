import math
import pickle
import glob
def ecludin(vec1,vec2):
    vec=set(vec1.keys()) | set(vec2.keys())
    b=0
    for i in vec:
        if i in vec1.keys():
            s=int(vec1[i])
        else:
            s=0
        if i in vec2.keys():
            r=int(vec2[i])
        else:
            r=0
        a=pow((float(s)-r),2)
        b=b+a
    c=math.sqrt(b)
    return c

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
        euc=ecludin(vec1,vec2)
        print "euclidien dis b\w   ",name,"and  ",name1,"is ",euc
        g.close()
    f.close()
