import numpy as np

print("-------------- MATRIX ADDITION ---------------")
print()
a = np.array([[1,2,3],
              [4,5,6]])

b = np.array([[10,11,12],
              [13,14,15]])

c = a + b #matrix addition

print(c)
print("______________________________________________")


print("-------------- MATRIX ADDITION ---------------")
print()
a = np.array([[1,2,3],
              [4,5,6]])

b = np.array([[10,11,12],
              [13,14,15]])

c = a * b

print(c)
print("______________________________________________")

print("-------------- Identity Matrix ---------------")
print()

i = np.eye(4)
print(i)
print("______________________________________________")



print("-------------- Redimensioning array ---------------")
print("convert 1d to 3d array")
print()

a = np.array([x for x in range(27)])
b = a.reshape((3, 3, 3))

print(b)
print("______________________________________________")