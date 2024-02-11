import numpy as np


#ARRAY CREATION FROM LIST
# listnum = np.array([[1, 2, 3,], [4, 5, 11], [7, 8, 9]])
# print(listnum)
# print(listnum.dtype)
# print(listnum.shape)
# print(listnum.size)

# listnum[1, 2] = 6

# print(listnum)

#ARRAY CREATION FROM NUMPY FUNCTIONS
# zeros = np.zeros((3, 3))
# print(zeros)
# print(zeros.dtype)

# arange = np.arange(15)
# print(arange)
# print(arange.dtype)
# print(arange.shape)

lspace1 = np.linspace(1, 4, 4)
# print(lspace1)

# lspace2 = np.linspace(1, 10, 20)
# print(lspace2)

# emp = np.empty((2, 3))
# print(emp)


# emp_like = np.empty_like(lspace1)
# print(emp_like)

id = np.identity(9)
print(id)
print(id.shape)