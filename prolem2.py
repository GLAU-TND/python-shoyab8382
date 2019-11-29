a=8
b="hello"
c=[1,2,3]
def aa(l=0):
    pass
print("1. TypeError")
print("2. AttributeError")
print("3. ValueError")
n=int(input())
if n==1:
    try:
        a+b
    except TypeError:
        print("TypeError occurred")
if n==2:
    try:
        b.remove("hel")
    except AttributeError:
        print("AttributeError occurred")
if n==3:
    try:
        raise ValueError
    except ValueError:
        print("ValueError occurred")
