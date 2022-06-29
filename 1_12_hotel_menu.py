## bill ............


count1=0
count2=0
count3=0
count4=0
count5=0
print("\n              Welcome\n")

print(" ################################")
print("       # Speacial Offer # ")
print(" --------------------------------")
print(" *  10 % discount on above 200 Rs")
print(" *  15 % discount on above 500 Rs")
print(" *  20 % discount on above 1000 Rs")
print(" ################################")
count=0
while count == 0:
    print("\n -------------------------------")
    print("               Menu ")
    print(" -------------------------------")
    print(" Press 1 : 40 Rs .... item1  ")
    print(" Press 2 : 70 Rs ....item2 ")
    print(" Press 3 : 100 Rs ....item3 ")
    print(" Press 4 : 50 Rs ....item4 ")
    print(" Press 5 : 75 Rs ....item5 ")
    print(" Press 6 : Exit from Menu ")
    print(" -------------------------------")

    counter = int(input(" : "))

    if( counter == 1 ):
        count1 = int(input(" Enter the quantity : "))
    elif( counter == 2 ):
        count2 = int(input(" Enter the quantity : "))
    elif( counter == 3 ):
        count3 = int(input(" Enter the quantity : "))
    elif( counter == 4 ):
        count4 = int(input(" Enter the quantity : "))
    elif( counter == 5 ):
        count5 = int(input(" Enter the quantity : "))

    count = int (input(" Do you want to continue...press 0 : "))
total = 40 * (count1) + 70 * (count2) + (count3) * 100 + 50 * (count4) + 75 * (count5)

print("\n #########################################")
print("-----------------------------------------")
print("                 Bill ")
print("-----------------------------------------")
print(" Items\t Quantity\t Rs")
if( count1 > 0):
    print(" item1\t   "+str(count1)+"\t\t"+ str(40 * (count1)))
elif( count2 > 0 ):
    print(" item2\t   "+str(count2)+"\t\t"+ str(70 * (count2)))
elif( count3 > 0 ):
    print(" item3\t   "+str(count3)+"\t\t"+ str(100 * (count3)))
elif( count4 > 0 ):
    print(" item4\t   "+str(count4)+"\t\t"+ str(50 * (count4)))
elif( count5 > 0 ):
    print(" item5\t   "+str(count5)+"\t\t"+ str(75 * (count5)))


print("\n Total\t\t\t" + str(total) + "\n")

if (total >= 200 and total < 500):
    total_bill = total - 0.1* total
    print(" --------------------------------\n Discount    10%\t"+str(0.1*total))
elif(total >= 500 and total < 1000):
    total_bill = total - 0.15* total
    print(" --------------------------------\n Discount    5%\t"+str(0.15*total))
elif(total >= 1000):
    total_bill = total - 0.20* total
    print(" --------------------------------\n Discount    20%\t"+str(0.20*total))
else:
    total_bill = total


print("\n --------------------------------") 
print("\n Total bill\t\t" + str(total_bill) + "\n")
print(" ################################")