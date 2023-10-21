import numpy as np

# # ==== dot(), matmul() - matrix multiplication
# a = np.arange(1, 10).reshape(3, 3)
# b = np.arange(10, 19).reshape(3, 3)
# print(np.dot(a, b))
# print(np.dot(b, a))
# # operator @ replaces  dot() function
# print(a @ b)
# print(b @ a)
#
# # !! this function is preferred
# print(np.matmul(a, b))
# print(np.matmul(b, a))

# # vector multiplication
# a = np.arange(1, 10)
# b = np.ones(9)
#
# # returns a number
# print(np.inner(a, b))
# # returns a matrix
# print(np.outer(a, b))

# ==== linalg module
a = np.array([(1, 2, 3), (1, 4, 9), (1, 8, 27)])
print(np.linalg.matrix_rank(a))

y = np.array([10, 20, 30])
# np.linalg.solve() solve a linear matrix equation, or system of linear scalar equations.
print(np.linalg.solve(a, y))

# inv() - returns inverse matrix
inv_a = np.linalg.inv(a)
print(inv_a)
