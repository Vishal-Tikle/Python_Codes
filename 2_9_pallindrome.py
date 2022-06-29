def pallindrome(string):
    reverse = string[::-1]
    if(reverse == string ):
        print(string,"is Palindrome")
    else:
        print(string,"is not palindrome")

str = input("Enter the string : ")
pallindrome(str) 
