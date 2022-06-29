class marks():
    def __init__(self):
        self.s1 = int(input("\n Enter the marks in Subject 1 : "))
        self.s2 = int(input(" Enter the marks in Subject 2 : "))
        self.s3 = int(input(" Enter the marks in Subject 3 : "))
        self.s4 = int(input(" Enter the marks in Subject 4 : "))
        self.s5 = int(input(" Enter the marks in Subject 5 : "))
    def displaymarks(self):
        print("\n Marks obtained in 5 subject : \n")
        print(" Subject 1  : ",self.s1)
        print(" Subject 2  : ",self.s2)
        print(" Subject 3  : ",self.s3)
        print(" Subject 4  : ",self.s4)
        print(" Subject 5  : ",self.s5)

class incentives():
    def __init__(self):
        self.incentive = int(input("Enter the Incentive Marks : "))
    def displayincentive(self):
        print(" Incentives : ",self.incentive)

class result(marks,incentives):
    def __init__(self):
        marks.__init__(self)
        incentives.__init__(self)
    def display_result(self):
        marks.displaymarks(self)
        incentives.displayincentive(self)
        self.total = self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.incentive
        self.percentage = self.total / 6
        print("\n-----------------------------")
        print(" Total Marks : ",self.total)
        print(" Percentage  : ",round(self.percentage,3))
        print("-------------***--------------")

r1 = result()
r1.display_result()