import numpy as np

a = np.array([10,20,30,40])
b = np.arange(4)

c = a - b
print(a,b,c)

d = b ** 2
print(d)

f = np.sin(a) * 10
print(f)

print(b<3)
print(b==3)

g = np.arange(4).reshape((2,2))
h = np.arange(8, 12).reshape((2,2))
print(g)
print(h)


i = g*h
j = np.dot(g,h)
k = g.dot(h)
print(i)
print(j)
print(k)


l = np.random.random((2,4))
print(l)

print(np.sum(l,axis=1))
print(np.min(l, axis=0))
print(np.max(l, axis=1))
