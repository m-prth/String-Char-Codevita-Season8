def find(x):
    e=0
    for j in range(0,x):
        if(c[j]==c[x]):
            e=e+1
    return e
a=int(input())
b=input()
c=[]
d=len(b)
m=[]
for i in range(0,d):
    c.insert(i,b[i])
Q=int(input())
P=[]
for i in range(0,Q):
    x=int(input())
    x=x-1
    P.insert(i,x)
    m.insert(i,find(x))

for i in range(0,Q):
    print(m[i])
