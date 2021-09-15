#frequency of characters of a string
string=input("enter a string")
setstring=set(string)
d={}
for i in setstring :
    d[i]=string.count(i)

print(d)
