import numpy as np

# python list differs from numpy array
# lst = [1, 2, 3]
# a = np.array([1, 2, 3])
# print(lst * 2)
# print(a * 2)

# print(-a)
# print(a - 3)
# print(a + 2)
# print(a * 5)
# print(a / 5)
# print(a // 3)
# print(a ** 3)
# print(a % 2)

# b = np.array([3, 4, 5])
# print(a + b)
# print(a - b)
# print(b - a)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a ** b)
# print(a % b)

# a + 10 doesn't change the array a but creates a copy of it, and a += 10 changes the array a
a = np.array([1, 2, 6, 8])
b = np.array([3, 4, 5, 6])
a += 5
print(a)

print((a + b) * 5 - 10)
