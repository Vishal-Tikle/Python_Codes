def get_details():
    print("\n Enter the Details of An Employee : ")
    global name , employee_id , dept , designation
    name = input(" Name\t\t\t: ")
    employee_id = int (input(" Employee ID\t\t: "))
    dept = input(" Department\t\t: ")
    designation = input(" Designation\t\t: ")

def calculate_salary():

    global basic_sal,HRA,TA,DA,incentive,PF_deduction,tax_tds,gross_sal
    basic_sal = float(input("\n Enter the Basic Salary : "))
    HRA = float(input(" Enter the HRA\t\t: "))
    TA = float(input(" Enter the TA\t\t: "))
    DA = float(input(" Enter the DA\t\t: "))
    incentive = float(input(" Enter the Incentive\t: "))
    PF_deduction = float(input(" Enter the PF Deduction\t: "))
    tax_tds = float(input(" Enter the TAX TDS\t: "))
    gross_sal = basic_sal + (HRA /100 * basic_sal ) + (TA /100 * basic_sal ) + (DA /100 * basic_sal ) + incentive - PF_deduction - tax_tds 


def put_details():
    print(" \n ---------------------------------------")
    print("========================================")
    print(" \t SALARY CERTIFICATE")
    print("========================================")
    print(" Details of an Employee are as follows : \n")
    print(" Name\t\t\t: ",name)
    print(" Employee ID\t\t: ",employee_id)
    print(" Department\t\t: ",dept)
    print(" Designation\t\t: ",designation)
    print(" \n ---------------------------------------")
    print(" Basic Salary\t\t: ",basic_sal)
    print(" HRA\t\t\t: ",(HRA /100 * basic_sal ))
    print(" TA\t\t\t: ",(TA /100 * basic_sal ))
    print(" DA\t\t\t: ",(DA /100 * basic_sal ))
    print(" Incentive\t\t: ",incentive)
    print(" Pf Deduction\t\t: ",PF_deduction)
    print(" Tax TDS\t\t: ",tax_tds)
    print(" \n ---------------------------------------")
    print(" Gross Salary\t\t: ",gross_sal)
    print(" \n ---------------------------------------")
    print("\t\t --*--")


choice = 'Y'
while choice == 'Y':
    get_details()
    calculate_salary()
    put_details()

    choice=input("\n Do you want to continue.....Y/N : ")