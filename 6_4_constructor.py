class student():
    no_of_student = 0
    def __init__(self,var):
        self.var = var
        print("\n Value of object variable : ",self.var)
        student.no_of_student += 1
        print("\n Value of class variable : ",student.no_of_student)


vishal = student(18)
bhushan = student(12)


# or
#print(vishal.no_of_student)
#print(vishal.var) 