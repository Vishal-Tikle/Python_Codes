developers = { "Pranay", "Vishal", "Mithilesh","Atharv"}
analysts = { "Sanket", "Kartik", "Sahil", "Venkat", "Vishal"}

print("\n* List of employees are as follows :")
print(developers.union(analysts))
print("\n* List of Developers are as follows :")
print(developers)
print("\n* List of Anlysts are as follows :")
print(analysts)
print("\n* List of employees which are Developers as well as Analysts are as follows :")
print(developers.intersection(analysts))
print("\n* List of employees which are Developers but not Analysts are as follows :")
print(developers.difference(analysts))
print("\n* List of employees which are Analysts but not Developers are as follows :")
print(analysts.difference(developers))

#symmetric difference
print(analysts.symmetric_difference(developers))
print("sorted list")
print(sorted(developers.union(analysts)))