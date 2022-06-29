class Person():
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
    
    def display(self):
        print(" Name    : ",self.Name)
        print(" Age     : ",self.Age)

class Publication():
    def __init__(self,papers, books, article):
        self.Papers = papers
        self.Books = books
        self.Articles = article

    def display(self):
        print(" Papers  : ",self.Papers)
        print(" Books   : ",self.Books)
        print(" Articles: ",self.Articles)


class Faculty(Person, Publication):
    def __init__(self, name , age , papers, books, article ):
        Person.__init__(self,name,age)
        Publication.__init__(self,papers, books, article)

    def display(self):
        print("\n Details of faculty are as follows : \n")
        Person.display(self)
        Publication.display(self)

r1 = Faculty("V",35,"E","c and c++", "electronics")

r1.display()