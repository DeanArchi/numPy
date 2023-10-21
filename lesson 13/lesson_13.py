import numpy as np

# a = np.array([1, 2, 3, 10, 20, 30])
# b = np.array([2])
#
# print(a * b)
# print(a + b)

# This works by broadcasting arrays:
# 1. if the arrays have a different number of axes, then new ones are added to the smaller array so that they match
# 2. the axes with 1 element are expanded so that the sizes of the 2 arrays match
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# b = np.array([4, 5, 6])
# print(a + b)
#
# a = np.arange(6).reshape(3, 1, 2)
# b = np.ones(4).reshape(2, 2)
# # a: 3 x 1 x 2
# # b: 2 x 2
# # c: 3 x 2 x 2
# c = a * b
# print(c.shape)

a = np.array([1, 2, 3])
b = np.array([4, 5])
c = np.array([7, 8, 9, 10])
# # in order to accomplish this equation you need to resize the arrays like this:
# # a: 1 x 1 x 3
# # b: 1 x 2 x 1
# # c: 4 x 1 x 1
# a.shape = 1, 1, -1
# b.shape = 1, -1, 1
# c.shape = -1, 1, 1
# d = a * b + c
# print(d)
# print(d.shape)
# !!!! to make it easier, you can use function ix_():
# !!!! ix_() applies only to one-dimensional arrays
an, bn, cn = np.ix_(a, b, c)
d = an * bn + cn
print(d)
print(d.shape)
