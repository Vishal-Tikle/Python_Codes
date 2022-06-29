#Construct a program to perform following opeartion on a list containing the item number of 
#sold spare part of an automobile shop
#List=[1,7,8,1,8,7,9,15,16,17,99,99,99,15,16]


List=[1,7,8,1,8,7,9,15,16,17,99,99,99,15,16]

print(" Original List ",List)
print("\n Quantity of item 15 sold : ",List.count(15))

list1=List
list1.pop()
print("\n Undated list ",list1)

list2=List
del(list2[6])
list2.insert(6,50)
print("\n Undated list ",list1)

list3=List
list3.sort()                                      #using sort() method
print("\n Sorded List : ",list3)
#list3=List                                              
#print("\n Sorded List : ",sorted(list3))          using sorded operation

#using Concatenate(+)
List1=[1,8,15,17,99]
list4=List+List1
print("\n Undated List + : ",list4)

#using extend method
list5=List
list5.extend(List1)
list5.sort()
print("\n Sorded updated List extend: ",list5)