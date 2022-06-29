class details():
    def __init__(self,name,dept,sec):
        self.name = name 
        self.dept  = dept
        self.sec = sec
    def display_details(self):
        print("-----------------------------")
        print("\t Result")
        print("-----------------------------")
        print(" Details of Student :\n")
        print(" Name       : ", self.name)
        print(" Department : ",self.dept)
        print(" Section    : ",self.sec)
        print("-----------------------------")

class marks():
    def __init__(self,s1,s2,s3,s4,s5):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
    def displaymarks(self):
        print(" Marks obtained in 5 subject : \n")
        print(" Subject 1  : ",self.s1)
        print(" Subject 2  : ",self.s2)
        print(" Subject 3  : ",self.s3)
        print(" Subject 4  : ",self.s4)
        print(" Subject 5  : ",self.s5)

class incentives():
    def __init__(self,incentive):
        self.incentive = incentive
    def displayincentive(self):
        print(" Incentives : ",self.incentive)

class result(marks,incentives):
    def __init__(self,name,dept,sec,s1,s2,s3,s4,s5,incentive):
        details.__init__(self,name,dept,sec)
        marks.__init__(self,s1,s2,s3,s4,s5)
        incentives.__init__(self,incentive)
    def display_result(self):
        details.display_details(self)
        marks.displaymarks(self)
        incentives.displayincentive(self)
        self.total = self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.incentive
        self.percentage = self.total / 6
        print("\n-----------------------------")
        print(" Total Marks : ",self.total)
        print(" Percentage  : ",round(self.percentage,3))
        print("-------------***--------------")



r1 = result("Vishal","ETC",'B',90,80,75,90,80,99)
r1.display_result()