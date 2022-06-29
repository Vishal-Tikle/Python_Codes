num = 10
print(type(num))     #type written in class 
# ans -> int 

# List is mutable whereas tuble is unmutable

x=1 
while True:
    if x%5==0:
        break
    print(x)
    x+=1

str = "Python"
print(str[-1:])

x='pqrs'
for i in range (len(x)):
    x[i].upper()
print(x)
 
l1=[]
l1.append([1,[2,3],4])
l1.extend([7,8,9])
print(l1[0][1][1]+l1[2])