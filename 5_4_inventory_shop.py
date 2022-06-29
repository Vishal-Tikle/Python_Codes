"""import pandas as pd
details = {
    'Name':['item1','item2','item3','item4','item5'],
    'Serial No':[100,101,102,103,104],
    'Price':[1000,2000,100,50,1000],
    'Quantity':[10,9,5,10,2]
}

details_item = pd.DataFrame(details)

print(details_item)

"""      #multiline commnad  using """ vishal """

#    OR

import pandas as pd
name = []
serial_no=[]
price =[]
quantity = []
details = {}

n = int(input("Enter the no of items : "))

for i in range (0,n):
    print("\n Enter the details of item are as follows \n")
    key=input(" Name : ")
    name.append(key)
    key=input(" Serial No : ")
    serial_no.append(key)
    key=input(" Price: ")
    price.append(key)
    key=input(" Quantity Available : ")
    quantity.append(key)
    
details_item = {'Name':name,
    'Serial No':serial_no,
    'Price':price,
    'Quantity':quantity}

details_of_item = pd.DataFrame(details_item)

print("\n")
print(details_of_item)