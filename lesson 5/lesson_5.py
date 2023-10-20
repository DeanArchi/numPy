import numpy as np

# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(a)
#  -1 means that the number of rows will be automatically calculated relative to the number of columns and vice versa
# a.shape = -1, 2
# print(a)
# a.shape = 2, -1
# print(a)
# a.shape = -1
# print(a)

# function ravel() converts a 2 dimensional array to a vector (1 dimensional)
# b = a.reshape(-1, 2)
# print(b.ravel())

# function resize() changes the representation of this array and changes numbers of elements
# a.resize(2, 5)
# print(a)
# a.resize(3, 3, refcheck=False)
# print(a)
# a.resize(4, 5, refcheck=False)
# print(a)

# matrix transposition (creates new representation not new array)
# a = np.array([[1, 1, 1], [2, 8, 17], [3, 5, 9]])
# print(a)
# b = a.T
# print(b)

# x = np.arange(1, 10)
# x.shape = 1, -1
# print(x)
# y = x.T
# print(y)

# Adding and removing axes by functions: expand_dims and squeeze
a = np.arange(32).reshape(8, 2, 2)
print(a)
# expand_dims() creates new representation, the data is the same in the array a
b = np.expand_dims(a, axis=0)
c = np.expand_dims(b, axis=-1)
print(c.shape)
# squeeze removes all axes that have only 1 element
d = np.squeeze(c)
print(d.shape)

