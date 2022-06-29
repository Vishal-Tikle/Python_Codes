num=int(input("\n Enter the number : "))
temp=num
count=1
while count<temp:
    num= count * num
    count+=1

print("\n Factorial of "+ str(temp)+" is "+ str(num))