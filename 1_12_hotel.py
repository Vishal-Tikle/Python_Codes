count1=0
count2=0
count3=0
count4=0
count5=0

count=0
while count == 0:
    print("              Welcome")

    print(" ################################")
    print("               Menu ")
    print(" -------------------------------")
    print(" Press 1 : 40 Rs .... item1  ")
    print(" Press 2 : 70 Rs ....item2 ")
    print(" Press 3 : 100 Rs ....item3 ")
    print(" Press 4 : 50 Rs ....item4 ")
    print(" Press 5 : 75 Rs ....item5 ")
    print(" Press 6 : Exit from Menu ")
    print(" -------------------------------")

    counter = int(input(" Enter your input : "))

    if( counter == 1 ):
        count1 += 1
    elif( counter == 2 ):
        count2 += 1
    elif( counter == 3 ):
        count3 += 1
    elif( counter == 4 ):
        count4 += 1
    elif( counter == 5 ):
        count5 += 1

    count = int (input(" Do you want to continue...press 0 : "))
total = 40 * (count1) + 70 * (count2) + (count3) * 100 + 50 * (count4) + 75 * (count5)
print("\n Total bill : " + str(total) + "\n")


if (total > 200 and total < 500):
    total_bill = total - 0.1* total
elif(total >500 and total < 1000):
    total_bill = total - 0.15* total
elif(total >1000):
    total_bill = total - 0.20* total
else:
    total_bill = total

print("\n ################################")
print("\n Total bill : " + str(total_bill) + "\n")
print(" ################################")