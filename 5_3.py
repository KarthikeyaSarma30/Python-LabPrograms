s=input("enter a string")
count=0
words=s.split(" ")
for i in words :
    count+=1
print(count,end=" ")
print(words)
for i in words:
    print(i[::-1],end=" ")
