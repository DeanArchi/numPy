import numpy as np

# === array properties ===
# a = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
# print(a.dtype)
# a.dtype = np.int8()
# print(a.dtype)
# print(a)

# to find out the number of elements in an array
# print(a.size)
# to find out the size of the element
# print(a.itemsize)
# to find out the size of the array
# print(a.size * a.itemsize)

# a = np.ones((3, 4, 5))
# reshape does not create a new array, but creates a new representation of the original data
# b = a.reshape(3, 2, 10)
# print(a)
# print(b)
# !!!!!!! arrays a and b refer to different representations of the same array !!!!!!!
# to find out the number of array axes
# print(a.ndim)
# to find out the number of elements on each axis
# print(a.shape)
# using shape, you can change the representation of the same data of the current array
# a.shape = 60
# print(a)
# a.shape = (12, 5)
# print(a)

# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# view creates a copy of the representation of array a in array b
# b = a.view()
# a.shape = 3, 3
# print(a)
# print(b)

# creating a copy of the new array
# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# b = np.array(a)
# c = a.copy()
