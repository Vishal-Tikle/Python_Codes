class info():
    def __init__(self,name,no):
        self.name = name 
        self.no = no

    def display(self):
        print("\n Details of Item:")
        print("\n Item name\t:",self.name)
        print(" Item No.\t:",self.no)

class details(info):
    def __init__(self, name, no, stock, price):
        info.__init__(self, name, no)
        self.stock = stock 
        self.price = price 
    
    def display_d(self):
        info.display(self)
        print(" Stock\t\t:",self.stock)
        print(" Price\t\t:",self.price)

class items(details):
    def __init__(self, name, no, stock, price):
        details.__init__(self, name, no, stock, price)

    def display_data(self):
        details.display_d(self)

name = input("Enter item name : ")
no = int(input("Enter the no of item : "))
stock = int(input("Enter the stock of item :"))
price = float(input("Enter the price of item : "))


i1 = items(name,no,stock,price)
i1.display_data()
