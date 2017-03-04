import math
import pickle
import glob
def pearson(vec1,vec2):
    vec=set(vec1.keys()) | set(vec2.keys())
    N = len(vec)
    b=0
    c=0
    d=0
    h=0
    k=0
"""cd=0
up =0
low1 = 0
low2 = 0
mult_low = 0
result = 0"""
       for i in vec:
        if i in vec1.keys():
            s=int(vec1[i])
        else:
            s=0
        if i in vec2.keys():
            r=int(vec2[i])
        else:
            r=0
        a=s*r
        b=b+a
        c=c+s
        d=d+r
        e=pow(s,2)
        h=h+e
        l=pow(r,2)
        k=k+l
    cd = (c*d)/N
    up = b - cd
    low1 = h - ((c*c)/N)
    low2 = k-((d*d)/N)
    mult_low = math.sqrt(low1 * low2)
    result = up / mult_low
    print result
        

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
        pear=pearson(vec1,vec2)
        print "euclidien dis b\w   ",name,"and  ",name1,"is ",pear
        g.close()
    f.close()
