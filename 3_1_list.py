list_1 = [ 1, 2 , 3 , 4 , 5]
list_2 = [ 'A' , 'B' , 'C' , 'D' , 'E']
list_3 = [ "great", "going", "with" , "python"]
                              # Output
print(list_1[0])              # 1
print(list_2[::2])            # C
print(list_3[2:])             # with python
print(list_1[:])              # [ 1, 2 , 3 , 4 , 5]
list_1[3]=18
print(list_1)                 # [ 1, 2 , 18 , 4 , 5]
print(list_1[::-1])           # [5, 18, 3, 2, 1]
print(list_1[-1])             # 5
print(list_1[2],list_1[4])    # 3 5
print(list_2[1::3])           # B E