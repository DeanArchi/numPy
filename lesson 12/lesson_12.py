import numpy as np

# a = np.array([1, 2, 3, 4, 4, 3, 2, 1])
# # ==== unique() - converts an array to a set
# set_a = np.unique(a)
# print(set_a)
# # !! parameter return_counts=True return the number of times each unique item appears
# print(np.unique(a, return_counts=True))
# # !! parameter return_index=True return the indices of input array that result in the unique array.
# print(np.unique(a, return_index=True))
# # !! parameter return_inverse=True return the indices of the unique array that can be used to reconstruct input array
# print(np.unique(a, return_inverse=True))

# # a way to restore an array from a set:
# set_b, index = np.unique(a, return_inverse=True)
# print(set_b)
# print(index)
# set_b = set_b[index]
# print(set_b)

# ==== operations on sets
x = np.array([0, 1, 2, 3])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# == in1d() shows the occurrences of array x in array Y
print(np.in1d(x, y))

# == intersect1d() - intersection of sets
print(np.intersect1d(x, y))

# == union1d() - union of sets
print(np.union1d(x, y))

# == setdiff1d() - difference of sets
print(np.setdiff1d(x, y))
print(np.setdiff1d(y, x))

# == setxor1d() - symmetric difference of sets
print(np.setxor1d(x, y))
