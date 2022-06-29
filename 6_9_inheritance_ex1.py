class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"""
        Name         -  {self.name}
        Age          -  {self.age} """)

class Engineer(Student):
    def __init__(self,name,age,stream,dept,section):
        Student.__init__(self,name,age)
        self.stream = stream
        self.dept = dept
        self.section = section
    def displaydata(self):
        print("\n** Details of Engineer : \n")
        Student.display(self)
        print(f"""
        Stream       -  {self.stream}
        Department   -  {self.dept}
        Section      -  {self.section}   
        """)

class Doctor(Student):
    def __init__(self,name,age,stream,dept,section):
        Student.__init__(self,name,age)
        self.stream = stream
        self.dept = dept
        self.section = section
    def displaydata(self):
        print("\n** Details of Doctor : \n")
        Student.display(self)
        print(f"""
        Stream       -  {self.stream}
        Department   -  {self.dept}
        Section      -  {self.section}   
        """)

E = Engineer("Vishal T",19,"Engineeering","ETC",'B')
D = Doctor("Vaishu T",17,"Medical","Pharmacy",'B')

E.displaydata()
D.displaydata()
