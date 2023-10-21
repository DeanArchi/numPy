import numpy as np

# a = np.array([1, 2, 3, 10, 20, 30])
# b = np.array([1, 2, 3, 4, 5, 6])

# print(a[a > 5])
# print(a > 5)
# print(a == b)
# print(a != b)
# print(a != 2)

# # ==== function greater(a, b) (a > b)
# print(np.greater(a, b))

# # ==== function less(a, b) (a < b)
# print(np.less(a, b))

# # ==== function equal(a, b) (a == b)
# print(np.equal(a, b))

# # !!!! next code returns error:
# if (a == b): print('a == b')
# # !!! to avoid use array_equal(a, b):
# if np.array_equal(a, b):
#     print('a == b')

# # ==== any() returns True if at least 1 element of the array satisfies the condition
# print(np.any(a > 5))
# print(np.any(a == 5))
# print(np.any(a == b))

# # ==== all() returns True if all elements of the array satisfy the condition
# print(np.all(a > 5))
# print(np.all(a > 0))
# print(np.all(a > b))

# # ==== isinf() checks if there is an inf value in the array
# b = np.array([1, 2, 3, np.inf, np.inf])
# print(np.isinf(b))

# # ==== isnan() checks if there is a nan value (not a number) in the array
# b = np.array([1, 2, 3, np.nan, np.nan])
# print(np.isnan(b))

# # !!!! we can delete all inf/nan value from array in this way:
# a = np.array([1, 2, 3, np.inf, 4])
# filer_array = np.isinf(a)
# a = a[~filer_array]
# print(a)
#
# a = np.array([1, 2, 3, np.nan, 4])
# filer_array = np.isnan(a)
# a = a[~filer_array]
# print(a)

# # !!!! isfinite() returns True only in place of a number
# a = np.array([1, 2, np.inf, np.inf, 3, np.nan, 4, np.nan])
# print(np.isfinite(a))
# filter_array = np.isfinite(a)
# a = a[filter_array]
# print(a)

# # ==== functions iscomplex() & isreal()
# a = np.array([1+2j, 3-4j, 5, np.inf, np.nan])
# print(np.iscomplex(a))
# # # !!!! inf and nan are equated to a real number
# print(np.isreal(a))

# # ==== function logical_and()
x = np.array([True, False, True, False])
y = np.array([True, True, False, False])
a = np.array([1, 0, 2, 0])
b = np.array([3, 4, 0, 0])
print(np.logical_and(x, y))
print(np.logical_and(a, b))

# # ==== function logical_or()
print(np.logical_or(x, y))
print(np.logical_or(a, b))

# # ==== function logical_not()
print(np.logical_not(x))
print(np.logical_not(a))

# # ==== function logical_xor()
print(np.logical_xor(x, y))
print(np.logical_xor(a, b))
