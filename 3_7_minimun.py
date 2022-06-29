def low_cost_item(list):
    low = list[0]
    for i in range (1,items):
        if(low > list[i] ):
            low = list[i]
    return low

global n 
list=[]
items = int(input(" Enter the no of elements : "))
for i in range(0,items):
    key=int(input())
    list.append(key)
print("Low cost item : ",low_cost_item(list))