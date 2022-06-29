class Marks():
    def __init__(self,sub1,sub2):
        self.sub1 = sub1
        self.sub2 = sub2
    
    def calculate_total(self):
        self.total = self.sub1 + self.sub2
        return self.total

class Incentives():
    def __init__(self,incent):
        self.incent = incent

    def get_inecntives(self):
        return self.incent


class Result(Marks, Incentives):
    def __init__(self, sub1, sub2, incent):
        Marks.__init__(self,sub1, sub2)
        Incentives.__init__(self,incent)

    def grade_total(self):
        total = Marks.calculate_total(self)
        incentive = Incentives.get_inecntives(self)

        self.grade_total = total + incentive

    def display(self):
        print("\n Grade Total Marks : ",self.grade_total)


r1 = Result(80,75,100)

r1.grade_total()
r1.display()