print("###########################################################################")
def f(x):
    return x*x
L=[]
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
print(L)

from functools import reduce
def add(x,y):
    return x+y
t=reduce(add,[1,3,5,7,9])
print(t)
print("__________________________________________________________________________")
names={'a':1,'b':2,'c':3}
names['d']=4
print(names['d'])