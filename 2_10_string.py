string = input("Enter the string\t\t\t: ")

l=len(string)
print("\n Length of given string\t\t\t: ",l)

print("\n Print string 10 times : ")
print("\n",string[:]*10)

print("\n First character of string\t\t: ",string[0])

print("\n First three character of string\t: ",string[0:3])

print("\n Last three character of string\t\t: ",string[l-3:])

print("\n Backward of string\t\t\t: ",string[::-1])

if(l >= 7):
    print("\n Seventh character of string\t\t: ",string[6])
else:
    print("\n String is very Short")

print("\n String without first and last character: ",string[1:l-1])

print("\n String in all caps\t\t\t: ",string.upper())                   # for upper case : string_name.upper()

str=string.replace('a','e')

print("\n String 'a replaced by 'e' \t\t:",str[:])