#Matrix operations using vectorization

import numpy as np
a = np.array([1,2,3])
print("type: %s" %type(a))
print("shape: %s" %a.shape)
print(a[0], a[1], a[2])
a[0] = 5
print(a)

b = np.array([[1,2,3], [4,5,6]])
print("\n shape of b:", b.shape)
print(b[0,0], b[0,1], b[1,0])

a = np.zeros((2,2))
print("All zeroes matrix:\n  %s"  %a)

b = np.ones((1,2))
print("\nAll ones matrix:\n  %s"  %b)

d = np.eye(2)
print("\nIdentity matrix:\n  %s"  %d)

e = np.random.random((2,2))
print("\nRandom matrix:\n  %s"  %e)
print("Vectorized sum example\n")
x = np.array([[1,2],[3,4]])
print("x:\n %s" %x)
print("sum: %s" %np.sum(x))
print("sum axis = 0: %s" %np.sum(x, axis=0))
print("sum axis = 1: %s" %np.sum(x, axis=1))



a = np.arange(10000)
b = np.arange(10000)

dp = np.dot(a,b)
print("Dot product:  %s\n"  %dp)

op = np.outer(a,b)
print("\n Outer product: %s\n" %op)

ep= np.multiply(a,b)
print("\n Element wise product: %s \n"  %ep)