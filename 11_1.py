#print each line in the file in reverse order
f=open("D:\pythonfiles.txt","r")
for line in f:
    print(line[::-1])
