#merging two lists into dictionary
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
#print(dict(zip(l1,l2)))
d={}
for i in range(len(l1)):
    d[l1[i]]=l2[i]
print(d)
        
