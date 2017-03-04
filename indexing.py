import pickle
import glob
path='j:\mtech\others\irws code\data\*.pickle'
files=glob.glob(path)
dictt={}
i=0
for name in files:
    f=open(name,"rb")
    dictt[i]=pickle.load(f)
    i=i+1
ls=[]
for i in range(len(dictt)):
    ls.extend(dictt[i].keys())
set(ls)
#print ls

ind={}
l=0
for i in ls:
    ll=[]
    for j in range(len(dictt)):
        if i in dictt[j].keys():
            ll.append(j)
    set(ll)        
    ind[i]=[ll]
    l=l+1
#print ind
lls=ind.keys()
for j in lls:
    print j,' lsit of doc. is ',ind[j]

    
    
    
