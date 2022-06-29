lower = 0
upper = 0 
file_name = input(" Enter the file name : ")
file_obj = open(file_name)
line = file_obj.read()
for char in line:
    if char.isupper() and char != '\n':
        upper +=1
    elif char.islower() and char != '\n':
        lower +=1
    else :
        continue

print(" No of search charactor lower case : ",lower)
print(" No of search charactor upper case : ",upper)