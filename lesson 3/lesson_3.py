import numpy as np

# 1. autocomplete functions

# ===== empty() function =====
# print(np.empty(4, dtype='float64'))
# print(np.empty((3, 3), dtype='int16'))


# ===== eye() function =====
# print(np.eye(4, dtype='int32'))
# print(np.eye(4, 2))


# ===== identity() function =====
# print(np.identity(5))


# ===== ones() function =====
# print(np.ones(4))
# print(np.ones((2, 3, 4)))


# ===== zeros() function =====
# print(np.zeros(3))


# ===== full() function =====
# print(np.full((3, 2), 7))

# 2. matrix creation functions

# ===== mat() function =====
# print(np.mat('1 2 3 4'))
# print(np.mat([1, 2, 3, 4]))
# print(np.mat('1 2 3; 4 5 6; 7 8 9'))


# ===== diag() function =====
# print(np.diag([1, 2, 3, 4]))
# print(np.diag([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))


# ===== diagflat() function =====
# print(np.diagflat([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))


# ===== tri() function =====
# print(np.tri(5, dtype='int32'))
# print(np.tri(4, 2, dtype='int32'))


# ===== tril() function =====
# print(np.tril([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))
# print(np.tril([1, 2, 3]))


# ===== triu() function =====
# print(np.triu([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))
# print(np.triu([1, 2, 3]))


# ===== vander() function =====
# print(np.vander([1, 2, 3]))

# 3.functions for forming numerical ranges

# ===== arange() function =====
# print(np.arange(5))
# print(np.arange(1, 6))
# print(np.arange(1, 6, 2))


# ===== linspace() function =====
# print(np.linspace(1, 10, 0))
# print(np.linspace(1, 10, 1))
# print(np.linspace(1, 10, 2))
# print(np.linspace(1, 10, 3))
# print(np.linspace(1, 10, 4))


# ===== logspace() function =====
# print(np.logspace(0, 1, 3))


# ===== geomspace() function =====
# print(np.geomspace(1, 16, 5))

# 4. functions for forming arrays based on data

# ===== array() function =====
# a = np.array([(1, 2), (3, 4)])
# print(a)


# ===== copy() function =====
# b = np.copy(a)
# print(b)
# b[0, 0] = 9
# print(a)
# print(b)


# ===== fromfunction() function =====
# def sum_numbers(x, y):
#     return x + y
#
#
# c = np.fromfunction(sum_numbers, (3, 3))
# print(c)
#
# print(np.fromfunction(lambda x, y: x * 50 + y, (2, 2)))


# ===== fromiter() function =====
# print(np.fromiter('hello', dtype='U1'))


# ===== fromstring() function =====
# print(np.fromstring('1 2 3', dtype='int16', sep=' '))
