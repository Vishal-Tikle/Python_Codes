import pandas as pd
 
n= int(input(" Enter the No of employees : "))
name = []
Dept = []
Emp_id = []
Desgn = []
basic_sal =[]
hra = []
ta = []
da = []
Incentive = []
Gross_sal = []
PF_deduction = []
TDS_deduction = []
Net_sal = []

student = {}

for i in range(0,n):
    print("\n Enter the Details are as follows :")

    key=input("Name : ")
    name.append(key)

    key=input("Department : ")
    Dept.append(key)

    key=int(input("Employee Id : "))
    Emp_id.append(key)

    key=input("Designation : ")
    Desgn.append(key)

    key=int(input("Basic Salary : "))
    basic_sal.append(key)

    key=int(input("HRA : "))
    hra.append(key)

    key=int(input("TA : "))
    ta.append(key)

    key=int(input("DA : "))
    da.append(key)

    key=int(input("Incentive : "))
    Incentive.append(key)
    gross_sal= int(basic_sal[i])+(hra[i])+(ta[i])+(da[i])+(Incentive[i])
    Gross_sal.append(gross_sal)

    key=int(input("PF deduction : "))
    PF_deduction.append(key)

    key=int(input("TDS deduction : "))
    TDS_deduction.append(key)

    TDS_deduction.append((Gross_sal[i])-(PF_deduction[i])-(TDS_deduction[i]))

student = {"Name":name,"Department":Dept,"Employee ID ":Emp_id,"Designation":Desgn,"Basic Salary":basic_sal,"HRA":hra,"TA":ta,"DA":da,"Incentive":Incentive,"Gross Salary":Gross_sal,"PF Deduction":PF_deduction,"TDS Deduction":TDS_deduction,"Net Salary":Net_sal}

student_de= pd.DataFrame(student)

print(student_de)