class number():
    num = []
    even = []
    odd = []
    zeros = 0
    positive = 0
    negative = 0


    def __init__(self,n):
        self.num = n
    def even_or_odd(self):
        for i in self.num:
            if(i % 2 == 0 ):
                print(i,"is Even number.")
                self.even.append(i)
            else:
                print(i,"is Odd number.")
                self.odd.append(i)
    def positive_zero_negative(self):
        for i in self.num:
            if i == 0:
                self.zeros += 1
            elif i > 0:
                self.positive += 1
            else:
                self.negative += 1
        print("\nNo of zeros : ",self.zeros)
        print("No of positive numbers : ",self.positive)
        print("No of negative numbers : ",self.negative)


list = []
n = int(input(" Enter the no of terms : "))

for i in range (0,n):
    key=int(input("Enter the number : "))
    list.append(key)


num1 = number(list)
num1.even_or_odd()
num1.positive_zero_negative()
print("\n List of Even ")
print(num1.even)
print(" List of Even ")
print(num1.odd)


"""
## sir 

choice = "Y"
while choice =="Y":
    num = int(input("Enter the number : "))
    obj1 = even_odd()

    obj1.check(num)
    choice = input("Do you wnat to continue ....Y/N... : ")
    if choice =="Y":
        continue
    else:
        break
print("\n List of Even ",obj1.even)
print(" List of Even ",obj1.odd)"""