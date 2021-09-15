#number in words
n=int(input("enter a number"))
reverse=0
while n!=0 :
    r=n%10
    reverse=reverse*10+r
    n=n//10
while reverse!=0 :
    r=reverse%10
    if r==1 :
        print("one",end="")
    elif r==2 :
        print("two",end="")
    elif r==3 :
        print("three",end="")
    elif r==4 :
        print("four",end="")
    elif r==5 :
        print("five",end="")
    elif r==6 :
        print("six",end="")
    elif r==7 :
        print("seven",end="")
    elif r==8 :
        print("eight",end="")
    elif r==9 :
        print("nine",end="")
    else :
        print("zero",end="")
    reverse=reverse//10

    
