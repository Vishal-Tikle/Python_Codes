num=int (input("Enter any number : "))
temp=num
rev=0

while(num>0):
    d1=num%10
    rev=(rev*10)+d1
    num=(num-d1)/10

if temp==rev:
    print(temp,"is pallidrome")
else:
    print(temp,"is not pallidrome")
