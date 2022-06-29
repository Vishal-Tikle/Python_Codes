class number():
    even= []
    odd = []
    def __init__(self,num):            # constructor 
        if num % 2 == 0:
            self.even.append(num)
        else :
            self.odd.append(num)

n = int(input("Enter the no of elements :"))

for i in range(1,n+1):
    obj = number(i)

print(obj.even)
print(obj.odd)