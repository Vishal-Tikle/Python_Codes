import numpy as np
mat = np.array([[1,2,3],[4,5,6]])

print(" Dimension of matrix :",mat.ndim)
print(" Size of matrix :",mat.size)
print(" Shape of matrix :",mat.shape)
print(" Datatype of matrix :",mat.dtype)

print(" Second element of second row :",mat[1,1])
print(" Third element of first row :",mat[0,2])
print(" Matrix : \n")
print(mat)

del(mat[1,1])
mat.insert([1,1],10)
print("Updated Matrix : \n")
print(mat)