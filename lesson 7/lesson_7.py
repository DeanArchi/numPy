import numpy as np

# a = np.arange(11)
# print(a[0])
# print(a[-11])
# print(a[-1])

# b = a[2:5]
# print(b)
# b = a[3:]
# print(b)
# b = a[:3]
# print(b)
# b = a[::2]
# print(b)

# a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
# print(a[1, 1])
# print(a[-1, -1])
# print(a[0])
# print(a[2, :])
# print(a[:, 1])

# ==== flat() lines up all the elements of a multidimensional array into a vector
# standard method
# for row in a:
#     for value in row:
#         print(value, end=' ')
# print()
# with flat()
# for value in a.flat:
#     print(value, end=' ')

# ==== list indexing
a = np.arange(2, 18)
# created copy of array a (b doesn't depend on array a)
b = a[[0, 1, 7, 8, 9]]
print(b)
c = a[a > 8]
print(c)
