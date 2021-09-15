#mean,modian,mode of a list
l=[1,2,3,4,4,5,5,5,5,6,6,7,8]
def mean(l):
    meanl=sum(l)/len(l)
    print(meanl)
def median(l):
    l.sort()
    n=len(l)
    if(len(l)%2!=0):
        median=l[int((n-1)/2)]
    else:
        median=l[int(n/2)]+l[int((n-1)/2)]
    print(median)
def mode(l):
    lset=set(l)
    print(lset)
    d={}
    for i in lset:
        d[l.count(i)]=i
    print(d)
    mode=max(d.keys())
    print(d[mode])
mean(l)
median(l)
mode(l)

        
