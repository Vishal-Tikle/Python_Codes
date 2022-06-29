class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(" Name : ",self.name)
        print(" Age : ",self.age)

class Teacher(person):
    def __init__(self,name,age,exp,qual):
        person.__init__(self,name,age)
        self.exp = exp
        self.qual = qual
    def displaydata(self):
        print("\n** Details of Teacher : \n")
        person.display(self)
        print(" Experience : ",self.exp)
        print(" Qualification : ",self.qual)

class Student(person):
    def __init__(self,name,age,dept,sec):
        person.__init__(self,name,age)
        self.dept = dept
        self.sec = sec
    def displaydata(self):
        print("\n** Details of Student : \n")
        person.display(self)
        print(" Department : ",self.dept)
        print(" Section : ",self.sec)

T = Teacher("Vivek D",34,16,"M.Tech")
s = Student("Vishal T",19,"ETC",'B')

T.displaydata()
s.displaydata()
