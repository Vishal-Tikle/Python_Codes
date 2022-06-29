def ispallindrome(string):
    l=int(len(string)/2)
    str1 = string[:l]
    str2 = string[l+1:]
    reverse = str2[::-1]

    if (str1 == reverse):
        return True
    else:
        return False

str = input("Enter the string : ")
if(ispallindrome(str)):
    print(str,"is pallindrome")
else:
    print(str,"is not pallindrome")