class MyException(Exception):
    pass
def xyz(a,b):
    if(a+b)<150:
        raise MyException("Custom Exception Occurred")
    else:
        print(a+b)
a=int(input())
b=int(input())
xyz(a,b)
