def prime(n) :
    if n<=1 :
        return False
    for i in range(2,int(n/2)+1) :
        if(n%i==0):
            return False
    return True
s=0
for i in range(2,2000000) :
    if(prime(i)==True):
        s+=i
print(s)
        
