# Dictionary

student = { "Roll no":"2022/44","Name":"Vishal", "Section":'B', "Branch":"ETC"}

print("\n Details of Student : \n")
print(" * Name\t   : ",student["Name"])
print(" * Roll No.: ",student["Roll no"])
print(" * Section : ",student["Section"])

# method 2 : dict()
print(dict([('roll no','2022/44'),('Section','B')]))

# method 3 : comprehension
square = { x : x**2 for x in range(1,5)} 
print(square)