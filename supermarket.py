class Mysupermarket:
    product_code = []
    product_name = []
    cost_price = []
    product_quant = []

    def getdata(self):
        self.p = int(input("Enter no. of Products you need to Store:"))
        for i in range(self.p):
            self.product_code.append(int(input("Enter product code:")))
            self.product_name.append(str(input("Enter product Name:")))
            self.cost_price.append(float(input("Enter Cost Price:")))  # Changed int to float for cost price

    def display(self):
        print("Stock In Stores")
        print("---------------------------------------------------")
        print("Productcode \t Product Name \t Cost Price")
        print("---------------------------------------------------")
        for i in range(self.p):
            print(self.product_code[i], "\t\t", self.product_name[i], "\t\t", self.cost_price[i])
        print("---------------------------------------------------")

    def printbill(self):
        total = 0
        for i in range(self.p):
            q = int(input("Enter the quantity for the product code %d:" % self.product_code[i]))
            self.product_quant.append(q)
            total = total + self.cost_price[i] * self.product_quant[i]
        print("Receipt")
        print("---------------------------------------------------")
        print("Productcode \t Product Name \t Cost Price \t Quantity \t Total Amount")
        for i in range(self.p):
            print(self.product_code[i], "\t\t", self.product_name[i], "\t\t", self.cost_price[i], "\t\t",
                  self.product_quant[i], "\t\t", self.product_quant[i] * self.cost_price[i])
        print("---------------------------------------------------")
        print("Total amount =", total)


S = Mysupermarket()
S.getdata()
S.display()
S.printbill()

"""class 1-supermarket,class 2 food store(supermarket)"""
