file_obj = open("Info.txt","r")
vowels=0
consonants=0

line = file_obj.read()
for char in line:
    if(char in "aeiou"):
        vowels = vowels+1
    else:
        consonants += 1
print(vowels)
print(consonants)