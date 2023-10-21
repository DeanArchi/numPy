import numpy as np

# # ==== functions sum() mean() min(), max()
# a = np.array([1, 2, 3, 10, 20, 30])
# # sum() returns sum of all elements
# print(a.sum())
# # mean() returns the arithmetic mean of the array
# print(a.mean())
# print(a.min())
# print(a.max())
#
# a.resize(3, 2)
# print(a)
# print(a.sum(axis=0))
# print(a.sum(axis=1))

# # ==== functions abs(x), round(x), argmax(x), argmin(x)
# a = np.array([-1, 1, 5, -44, 32, 2])
# # abs() calculates the module of all elements or exact number
# print(np.abs(a))
# print(np.abs(a[3]))
# # round()
# print(np.round([1, 2, 3.3, 3.7, 5.1, 6]))
# # argmax() return index of the biggest element
# print(np.argmax(a))
# # argmin() return index of the smallest element
# print(np.argmin(a))

# # ==== functions sin(x), cos(x), tan(x)
# # linspace create an array in the interval from 0 to PI, which is divided into 10 parts
# a = np.linspace(0, np.pi, 10)
# print(np.sin(a))
# print(np.cos(a[3]))
# print(np.tan([0, 3.14]))

# # ==== functions np.random.rand(x), np.random.randint(x), np.random.randn(x), np.random.shuffle(x), permutation(x)
# # values from 0, 0.1, ..., 1
# print(np.random.rand())
# print(np.random.rand(5))
# print(np.random.rand(2, 3))
#
# # values from 0 to 10
# print(np.random.randint(10))
# # values from 5 to 10
# print(np.random.randint(5, 10))
# print(np.random.randint(5, size=4))
# print(np.random.randint(5, 15, size=(2, 3)))

# # generate array with size 5
# print(np.random.randn(5))

# a = np.arange(10)
# np.random.shuffle(a)
# print(a)
#
# # randomly permute a sequence, or return a permuted range.
# print(np.random.permutation(10))

# # ==== functions median(x), var(x), std(x), corrcoef(x), correlate(x), cov(x)
# x = np.array([1, 4, 3, 7, 10, 8, 14, 21, 20, 23])
# y = np.array([4, 1, 6, 9, 13, 11, 16, 19, 15, 22])
#
# # median() - returns the median of the array elements
# print(np.median(x))
#
# # var() - returns the variance of the array elements, a measure of the spread of a distribution
# print(np.var(x))
#
# # std() - returns the standard deviation, a measure of the spread of a distribution, of the array elements
# print(np.std(x))
#
# # corrcoef() - return Pearson product-moment correlation coefficients.
# xy = np.vstack([x, y])
# print(np.corrcoef(xy))
#
# # cov() - estimate a covariance matrix, given data and weights.
# print(np.cov(xy))
#
# # correlate()
# print(np.correlate(x, y))
