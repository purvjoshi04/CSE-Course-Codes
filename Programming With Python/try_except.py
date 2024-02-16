import sys


try:
    x=input("enter any number:")
    print(x+1)
except:
    print("Not a valid input")
    print("The exception occured is:",sys.exc_info()[2])
    print("The type return by method is:",type(sys.exc_info()))  

finally:
    print("hello")




