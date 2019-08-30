n=int(input())
a=list(map(int,input().split(" ")))
a.sort()
l=[]
b=set(a)
for i in b:
    l.append(a.count(i))
print((max(l)))

