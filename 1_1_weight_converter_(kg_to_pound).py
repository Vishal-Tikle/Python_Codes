weight_kg = float(input('\n Enter the Weight in Kg : '))
weight_pound  =2.2 * weight_kg
print(" Weight in pound : "+ str(weight_pound))

if weight_pound < 120.0:
    print('\n You are Under weight\n')
else:
    print('\n You have appropriate weight\n')