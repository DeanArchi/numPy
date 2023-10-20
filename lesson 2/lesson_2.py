import numpy as np

a = np.array([1, 2, 3, 4], 'float64')
# print(a)

# to see what types numpy supports
# print(np.sctypeDict)

# type conversion
# print(np.complex64(10))

# a = np.array([[1, 2], [3, 4], [5, 6]])
# print(a)

a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print(a)
print(a[1, 1, 0])
