import pandas as pd
 
n= int(input(" Enter the No of employees : "))
name = []
Dept = []
Emp_id = []
Desgn = []
basic_sal =[]
student = {}

for i in range(0,n):
    key=input("Name : ")
    name.append(key)
    key=input("Department : ")
    Dept.append(key)
    key=int(input("Employee Id : "))
    Emp_id.append(key)
    key=input("Designation : ")
    Desgn.append(key)
    key=input("Basic Salary : ")
    basic_sal.append(key)
    


student = {"Name":name,"Department":Dept,"Employee ID ":Emp_id,"Designation":Desgn,"Basic Salary":basic_sal}

student_de= pd.DataFrame(student)

print(student_de)