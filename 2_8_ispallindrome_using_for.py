def ispallindrome(string):
    for i in range(0,int(len(string)/2)):
        if(string[i] != string[len(string)-i-1]):
            return False
        else:
            return True

str = input("Enter the string : ")
if(ispallindrome(str)):
    print(str,"is pallindrome")
else:
    print(str,"is not pallindrome")
