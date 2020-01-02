import numpy as np

a = np.array([2,23,4], dtype=np.float)
print(a.dtype)

b = np.array([
        [1,2,3],
        [4,5,6]
    ])
print(b)


c = np.zeros((3,4))
print(c)

d = np.ones((3,4), dtype=np.float)
print(d)

f = np.empty((3,4), dtype=np.float)
print(f)

g = np.arange(10,20,2)
print(g)

h = np.arange(12).reshape((3,4))
print(h)

i = np.linspace(1, 10, 6).reshape((2,3))
print(i)
