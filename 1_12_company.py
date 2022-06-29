total=0
available_items1=10
available_items2=10
count1=0
count2=0
print("#####################################")
print("\tWelcome in SIMPLE ONE")
print("#####################################")
counter ='Y'
while counter == 'Y':
    print("\n Items\t\t\tRs \t Avilability")
    print("1 : item1   .....       100 Rs\t\t"+str(available_items1))
    print("2 : item2   .....       50 Rs\t\t"+str(available_items2))
    choice = int (input(" : "))

    if choice ==1:
        count1=int(input("\n Enter the Quantity : "))
        if(count1 <=available_items1):
            print("\n Available for delivery")
            available_items1 -=count1
        else:
            print("\n Unavailable") 
            
    elif choice ==2:
        count2=int(input("Enter the Quantity : "))
        if(count2 <=available_items2):
            print("\n Available for delivery")
            available_items2 -=count2

        else:
            print("\n Unavailable")
            
    else :
        break
    counter = input(" Do you want to continue...Press Y/N : ")

total = 100 * (count1) + 50 * (count2)

print("\n###############################")
print(" Items\tQuantity\tRs")
print(" -------------------------------")
if count1 > 0:
    print(" item1\t   "+str(count1)+"\t\t"+ str(100 * (count1)))
    
if count2 >0:
    print(" item2\t   "+str(count2)+"\t\t"+ str(50 * (count2)))
    
if(total > 50):


    if(total<5000):
        total_bill = total + 0.15 * total
        print(" GST \t\t15%\t"+ str(0.15*total))
    else:
        total_bill = total + 0.2222 * total
        print(" GST \t\t22%\t"+ str(0.2222*total))

    print("\n-------------------------------")
    print(" Delivery Tax\t\t: 200")
    print(" Swachha Bharat Abhiyan Tax : 10")
    print(" Girls Education Tax \t: 10")
    total_bill=total_bill + 220
else:
    total_bill =total

print(" -------------------------------")
print("\n Total Bill\t\t"+ str(total_bill))
print("\n-------------------------------")

