#exception handling
try:
    n1=int(input("enter a number"))
    n2=int(input("enter a number"))
    c=int(n1/n2)
    print("quotient",c)
except ZeroDivisionError :
    print("cant divide by zero")
except ValueError:
    print("improper data type")
