
def total_selling(list):
    sum=0
    for i in range(0,n):
        sum += list[i]
    return sum

list=[]
global n
n = int(input(" Enter the no of elements : "))
for i in range(0,n):
    key=int(input())
    list.append(key)
print("Total selling : ",total_selling(list))