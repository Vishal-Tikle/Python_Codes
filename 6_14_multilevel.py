class person():
    def __init__(self,name,dept):
        self.name = name 
        self.dept = dept

    def display(self):
        print("\n Details of Student :")
        print("\n Name\t\t:",self.name)
        print(" Department\t:",self.dept)

class details(person):
    def __init__(self, name, dept, year, section):
        person.__init__(self, name, dept)
        self.year = year 
        self.section = section 
    
    def display_d(self):
        person.display(self)
        print(" Year\t\t:",self.year)
        print(" Section\t:",self.section)

class student(details):
    def __init__(self, name, dept, year, section,sub1, sub2):
        details.__init__(self, name, dept, year, section)
        self.sub1 = sub1 
        self.sub2 = sub2

    def display_data(self):
        details.display_d(self)
        print("\n Marks obtained in following subject :\n")
        print(" Python Programming\t:",self.sub1)
        print(" Signal Proccessing\t:",self.sub2)

s1 = student("Vishal","ETC","2nd",'B',90,90)
s1.display_data()