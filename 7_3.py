l=[1,1,2,3,4,4,5,5,6,7,8]
def dup(l):
    l1=[]
    s=set(l)
    for i in s:
        if(l.count(i)>1) :
            l1.append(i)
    print(l1)
def unique(l):
    s=set(l)
    l1=[]
    for i in s:
        if l.count(i)==1:
            l1.append(i)
    print(l1)
dup(l)
unique(l)
