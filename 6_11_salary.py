class basic_salary():
    def __init__(self,basic_sal):
        self.basic_sal = basic_sal
    def display_basic_sal(self):
        print(" Basic salary : ",self.basic_sal)

class HRA():
    def __init__(self,hra):
        self.hra = hra
    def display_hra(self):
        print(" HRA\t: ",self.hra)

class TA():
    def __init__(self,ta):
        self.ta = ta
    def display_ta(self):
        print(" TA\t: ",self.ta)

class DA():
    def __init__(self,da):
        self.da = da
    def display_da(self):
        print(" DA\t: ",self.da)

class Incentive():
    def __init__(self,incentive):
        self.incentive = incentive
    def display_incentive(self):
        print(" Incentive : ",self.incentive)

class Salary():
    def __init__(self,basic_Sal,hra,ta,da,incentive):
        basic_salary.__init__(self,basic_Sal)
        HRA.__init__(self,hra)
        TA.__init__(self,ta)
        DA.__init__(self,da)
        Incentive.__init__(self,incentive)
        self.total_sal = self.basic_sal + self.hra + self.ta + self.da + self.incentive
    
    def display_salary(self):
        basic_salary.display_basic_sal(self)
        HRA.display_hra(self)
        TA.display_ta(self)
        DA.display_da(self)
        Incentive.display_incentive(self)
        print("\n Total Salary : ",self.total_sal)

s1 = Salary(100000,1000,2000,1000,5000)
s1.display_salary()