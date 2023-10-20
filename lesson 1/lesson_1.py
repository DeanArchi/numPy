import numpy as np

a = np.array([1, 2, 3, 4])

# print(a)
# print(a.dtype)
# print(a[2])

a[2] = 333
# print(a[2])

b = np.array([1, 2, "3", True])

# print(b)
# print(b.dtype)

c = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(c[[2, 2, 2, 2, 2, 2, 2]])
# print(c[[True, True, False, False, False, True, False, True, True]])

d = c.reshape(3, 3)
print(d)
print(d[0][2])
