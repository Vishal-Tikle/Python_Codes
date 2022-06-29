import pandas as pd

data = pd.read_csv("student_data.csv")

print(data['Name'])   # only print Name column elements 

print(data)      # whose file print