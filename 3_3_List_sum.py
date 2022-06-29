# Construct od Program to calculate the sum of all elements of following list 
# List_A = [1, 2, 3, 4, 5, 6, 7, 8, 9]

List_A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum=0
l=len(List_A)
i=0
while(i<l):
    sum += List_A[i]
    i += 1
print("Sum : ",sum)

# Using for loop
#List_A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#sum=0
#l=len(List_A)
#for i in range(0,l):
#    sum +=List_A[i]
#print("Sum : ", sum)