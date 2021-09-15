d={"ram":"12/3/2002","krishna":"14/5/2002","shiva":"18/5/2002"}
date=input("enter a string")
datesplit=date.split(" ")
print(datesplit)
datejoin="/".join(datesplit)
print(datejoin)
if datejoin in d.values():
    print("date of birth found in dictionary")
else:
    print("date of birth not found")
    
