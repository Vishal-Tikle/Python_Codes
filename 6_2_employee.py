class employee():
    basic_sal = 0                          # class variable
    hra = 0
    ta = 0
    da = 0
    incentive = 0
    total_sal = 0

    def get_details(self):
        # var = 0                        # object variable
        self.basic_sal = int(input("Enter the Basic salary : "))
        self.hra = int(input("Enter the HRA : "))
        self.ta = int(input("Enter the TA : "))
        self.da= int(input("Enter the DA : "))
        self.incentive = int(input("Enter the Incentive : "))

    def calculate_sal(self):
        self.total_sal = self.basic_sal + self.hra + self.ta + self.da + self.incentive

        return self.total_sal

    def display(self):
        print("Basic Salary : ",self.basic_sal)
        print("HRA : ",self.hra)
        print("TA : ",self.ta)
        print("DA : ",self.da)
        print("Incentive : ",self.hra)
        print("Total Salary : ",self.total_sal)

emp = employee()
for i in range(1,6):
    
    print("\n Enter Details of Employee ",i)
    emp.get_details()
    emp.calculate_sal()
    print("\n Details of Employee ",i)
    emp.display()