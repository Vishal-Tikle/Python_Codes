def salary(basic_sal):
    hra= 0.4*basic_sal
    ta=0.3*basic_sal
    da=0.9*basic_sal
    incentive=5000
    gross_sal = basic_sal + hra + ta + da
    return gross_sal

basic_sal = float(input(" Enter the basic salary of Employee : "))
net_sal = salary(basic_sal)
print(" Salary of the Employee : ",net_sal)