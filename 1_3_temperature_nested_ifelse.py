temp = float(input("\n Enter the Temperature : "))

if (temp >= -273) and (temp<=0):
    if(temp == -273):
        print("\n Absolute zero Temperature")
    elif(temp == 0):
        print("\n At Freezing Point")
    else:
        print("\n Below Freezing Point")

elif (temp > 0 ) and (temp <= 100):
    if(temp==100):
        print("\n Above Boiling Point")
    else:
        print("\n Normal Temperature")

elif(temp>100):
    print("\n Above Boiling Point") 
    
else:
    print("\n Invalid Temperature")