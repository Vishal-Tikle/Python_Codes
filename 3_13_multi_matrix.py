import numpy as np

mat1= np.array([[1,2],[4,5]])
mat2= np.array([[1,2],[4,5]])
mat3= np.array([[0,0],[0,0]])

for i in range (0,len(mat1)):
    for j in range (0,len(mat1)):
        for k in range (0,len(mat1)):
            mat3[[i],[j]] += mat1[[i],[k]] * mat2[[k],[j]]
print(mat3)