terms=float(input("Enter the no of terms : "))

if terms>0:                                           #validation
    count = 1
    while count <= terms:
        print((count ** 3)-1)                         # ** exponential operator
        count+=1
else:
    print("\n Kindly Enter valid input \n")



#num=1
#count =0
#while count < terms:
#        print((num ** 3)-1)                         # ** exponential operator
#        count+=1
#        num+=1
