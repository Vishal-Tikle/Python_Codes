class number():
    num = 0

    def __init__(self,n):
        self.num = n
    def even_or_odd(self):
        if(self.num % 2 == 0 ):
            print(self.num,"is Even number.")
        else:
            print(self.num,"is Odd number.")

n = int(input(" Enter the any integer : "))

num1 = number(n)
num1.even_or_odd()