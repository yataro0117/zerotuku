import numpy as np
A = np.array([1, 2, 3, 4])
print(A)
print(np.ndim(A)) #配列の次元数
print(A.shape) #配列の要素数
print(A.shape[0])
#行列の積
A = np.array([[5, 6], [7, 8]])
B = np.array([[1, 2], [3, 4]])
print(np.dot(A,B))

A = np.array([[5, 6], [7, 8], [9, 10]])
B = np.array([3, 4])
print(np.dot(A, B))