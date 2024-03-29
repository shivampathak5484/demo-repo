x=int(input("enter 1st no : "))
y=int(input("enter 2nd no : "))
try:
    print(x/y)
except IndexError:
    print("cannot divide")
except FileNotFoundError:
    print("doesnot found ")
except ZeroDivisionError:
    print("zero division error")