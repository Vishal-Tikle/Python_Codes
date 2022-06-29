class customer():
    count1 = 0
    count2 = 0
    count3 = 0
    total = 0

    def menu(self):
        print("\n***************** Restaurant *********************")
        print("\nSr no.\tItems     Price ")
        print("1.\titem1       100")
        print("2.\titem2       50")
        print("3.\titem3       75")

        
    def order(self):
        choice = int(input("Enter your choice : "))
        if choice == 1:
            self.count1 = int(input("Enter item1 quantity : "))
        elif choice == 2:
            self.count2 = int(input("Enter item2 quantity : "))
        elif choice == 3:
            self.count3 = int(input("Enter item3 quantity : "))
        
    def display_bill(self):
        print("\n#####################################\n")
        print(" Items\tQuantity\tRs\n")
        print(" -------------------------------")
        if self.count1 > 0:
            print(" item1\t   "+str(self.count1)+"\t\t"+ str(100 * (self.count1)))
    
        if self.count2 >0:
            print(" item2\t   "+str(self.count2)+"\t\t"+ str(50 * (self.count2)))
        if self.count3 >0:
            print(" item3\t   "+str(self.count3)+"\t\t"+ str(75 * (self.count3)))
        
        self.total = 100 * (self.count1) + 50 * (self.count2) + 75 * (self.count3)
        print(" -------------------------------")
        print("\n Total Bill\t\t"+ str(self.total))
        print("\n-------------------------------")
        print("#####################################")

customer1 = customer()
customer1.menu()

repeat = "Y"
while repeat == "Y":
    customer1.order()
    repeat = input("Do you want to continue .... Y/N   : ")

customer1.display_bill()