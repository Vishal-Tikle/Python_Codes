class student():
    name = ""
    dept = ""
    roll_no = 0
    year = 0
    section =""
    def get_details(self):
        self.name = input("Enter the Name : ")
        self.dept = input("Enter the Department : ")
        self.roll_no = int(input("enter the roll no : "))
        self.year = int(input("enter the year : "))
        self.section = input("Enter the section : ")
    def display(self):
        print("\nDetails of Student are as follows :")
        print("Name : ",self.name)
        print("Department : ",self.dept)
        print("Roll no : ",self.roll_no)
        print("Year : ",self.year)
        print("Section : ",self.section)
    
student1 = student()
student1.get_details()
student1.display()