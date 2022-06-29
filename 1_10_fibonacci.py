#Using while loop

count = float (input("\nEnter the no of terms : "))
first=0
second =1
counter =0

print ("\nThe fibonacci series are as follows : ")

while counter < count:
    print(first)
    temp=first
    first=second
    second=temp+first
    counter +=1



#using for loop

#count = int (input("\nEnter the no of terms : "))
#first=0
#second =1

#print ("\nThe fibonacci series are as follows")
#print("0 \n1 ")
#for counter in range(1,count-1,1):

#    print(first+second)
#    temp=first
#    first=second
#    second=temp+first



#count = float (input("\nEnter the no of terms : "))
#first=0
#second =1
#counter =0
#print ("\nThe fibonacci series are as follows")
#for counter in range(1,count):

#    print(first)
#    temp=first
#    first=second
#    second=temp+first
