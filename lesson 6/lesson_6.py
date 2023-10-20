import numpy as np

# ==== hstack([a, b]) - horizontal union
# a = np.array([(1, 2), (3, 4)])
# b = np.array([(5, 6), (7, 8)])
# c = np.hstack([a, b])
# print(c)

# ==== vstack([a, b]) - vertical union
# c = np.vstack([a, b])
# print(c)

# ==== column_stack([a, b]) - column union
# a = np.fromstring('1, 2, 3, 4', dtype='int16', sep=',')
# b = np.fromstring('5, 6, 7, 8', dtype='int16', sep=',')
# c = np.column_stack([a, b])
# print(c)

# ==== column_stack([a, b]) - row union
# c = np.row_stack([a, b])
# print(c)

# ==== concatenate - union by 2 or 3 etc. axes
# a = np.arange(1, 13)
# b = np.arange(13, 26)
# a.resize(3, 3, 2)
# b.resize(3, 3, 2)
#
# c0 = np.concatenate([a, b], axis=0)
# c1 = np.concatenate([a, b], axis=1)
# c2 = np.concatenate([a, b], axis=2)
# print(c2)

# ==== r_[] - translates slice objects to concatenation along the first axis.
# a = np.r_[0, [2, 3, 4], [5] * 3, 1:3]
# print(a)

# ==== r_[] - translates slice objects to concatenation along the second axis.
# a = np.c_[[1, 2, 3], [4, 5, 6]]
# print(a)

# ==== hsplit() - horizontal split
# a = np.arange(10)
# c, d = np.hsplit(a, 2)
# print(c)
# print(d)
# ==== vsplit() - vertical split
# a.shape = 10, -1
# print(a)
# c, d = np.vsplit(a, 2)
# print(c)
# print(d)

# ==== array_split() - split on an any axis
a = np.arange(18)
a.resize(3, 3, 2)
b, c = np.array_split(a, 2, axis=2)
print(b)
print(c)
