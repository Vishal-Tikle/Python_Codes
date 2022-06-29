import numpy as np

arr=np.array([1,2,3,4])
arr1=np.array([[1,2,3],[4,5,6]])
print(arr[2])                            # 3
print(arr[3])                            # 4
print(arr1[1,2])                         # 6

print(arr[0:2])                          # 1 2 
print(arr[1:2])                          # 2
print(arr[:2])                           # 1 2
print(arr[2:])                           # 3 4
print(arr[-1])
print(arr[::-1])
print("---------------\n")
print(arr1.ndim)                         # dimension
print(arr1.size)                         # size   6
print(arr1.shape)                        # shape  2*3
print(arr1.dtype)                        # datatype 