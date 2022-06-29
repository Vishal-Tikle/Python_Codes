class fibonacci():
    first = 0 
    second = 1
    third = 0

    def third_term(self):
        fibonacci.third = fibonacci.first + fibonacci.second
        print(fibonacci.third)
        
        fibonacci.first = fibonacci.second
        fibonacci.second = fibonacci.third

n = int(input(" Enter the no of terms : "))

print("\n Fibonacci series are as follows : ")
f1 = fibonacci()

if n ==1 :
    print(f1.first)
elif n == 2:
    print(f1.first)
    print(f1.second)
elif n > 2:
    i = 0
    print(f1.first)
    print(f1.second)
    while i < n-2: 
        f1.third_term()
        i += 1
else:
    print("Enter the valide no of terms.....")



"""or                            end="" use for print new statement in current line 
for i in range(0,n-2):
    f1.third_term()"""