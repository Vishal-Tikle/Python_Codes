def total(tuple_1):
    sum=0
    for i in range(0,len(tuple_1)):
        sum += tuple_1[i]                         # indexing using []  / slicing
    return sum

def min_amount(tuple_1):
    minimum=tuple_1[0]
    for i in range(0,len(tuple_1)):
        if(minimum > tuple_1[i]):
            minimum = tuple_1[i]
    return minimum

def max_amount(tuple_1):
    maximum=tuple_1[0]
    for i in range(0,len(tuple_1)):
        if(maximum < tuple_1[i]):
            maximum = tuple_1[i]
    return maximum

#both 
def min_max(tuple_1):
    minimum=tuple_1[0]
    maximum=tuple_1[0]
    for i in range(0,len(tuple_1)):
        if(minimum > tuple_1[i]):
            minimum = tuple_1[i]
        if(maximum < tuple_1[i]):
            maximum = tuple_1[i]
    return minimum,maximum


def min_amount(tuple_1):
    minimum=tuple_1[0]
    for i in range(0,len(tuple_1)):
        if(minimum > tuple_1[i]):
            minimum = tuple_1[i]
    return minimum
tuple_1 = (10000, 5000, 2000, 15000, 500, 450, 200, 20000)

print("\n Minimun amount : ",min(tuple_1))
print("\n Maximum amount : ",max(tuple_1))
print("\n Total amount \t: ",sum(tuple_1))

print("\n----------------------------------------")
print("\t\tUsing Fuction ")
print("----------------------------------------")
print("\n Minimun amount : ",min_amount(tuple_1))
print("\n Maximum amount : ",max_amount(tuple_1))
print("\n Total amount \t: ",total(tuple_1))

print("\n ------------------------------------------")
print("\n Maximum and maximum amount : ",min_max(tuple_1))
print("\n ------------------------------------------")