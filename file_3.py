count=0
file_name = input(" Enter the file name : ")
search_char = input(" Which char you want to search : ")
file_obj = open(file_name)
line = file_obj.read()

for char in line:
    if char == search_char:
        count +=1

print(" No of search charactor : ",count)
