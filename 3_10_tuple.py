def highest_mark(tuple1):
    high=tuple1[0]
    for i in range(0,len(tuple1)):
        if(high < tuple1[i]):
            high = tuple1[i]
    return high

def pass_count(tuple1):
    global count
    count =0
    for i in range (0, len(tuple1)):
        key=tuple1[i]
        per= float(key*2.5)
        if(per >= 50):
            count +=1
    return count

def result_function(tuple1):
    per = count /len(tuple1)*100
    return per

result=()
tuple1=(40,39,16, 18, 5, 8, 40, 37, 38)

print("\n Highest Mark obtained by student\t: ",highest_mark(tuple1))
print("\n Number of student pass\t\t\t: ",pass_count(tuple1))
print("\n Result of python programming\t\t: ",result_function(tuple1))

print("\n Sr No.\tMarks \t Percentage")
for i in range(0, len(tuple1)):
    key=tuple1[i]
    print(" ",i+1,"\t",tuple1[i],"\t ",float(key*2.5))