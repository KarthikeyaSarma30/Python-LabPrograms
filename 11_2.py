#find no of lines,words,characters
f=open("D:\pythonfiles.txt","r")
s=f.read()
print("no of characters:",len(s))
print("no of words:",len(s.split()))
print("no of lines:",len(s.split("\n")))
