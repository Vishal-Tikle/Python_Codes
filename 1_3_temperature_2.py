temp = float(input("\n Enter the Temperature : "))

if temp <-273:
    print(" Invalid temperature")
elif temp== -273: 
    print(" At freezing point")
elif(temp>-273)and (temp<0):
    print(" Below Freezing point")
elif temp== 0:
    print(" At freezing point")
elif(temp>0) and (temp<100):
    print("Normal Temperature")
elif temp==100 :
    print("At Boiling point")
else:
    print("Above Boiling point")