
#Problem Statement :- Create a Python program for inventory management. Initialize the inventory with two products, each with a name, quantity, and price. 
# Implement functionalities to display the inventory, add a new product, update a product's quantity, and calculate the total inventory value.



class inventory:
    def __init__(self):
        self.name=["Rice","Wheat"]
        self.quantity=[10,12]
        self.price=[1000,1500]

    def addProdName(self,name):
        self.name.append(name)
        
    
    def addProdQuantity(self,quantity):
        self.quantity.append(quantity)
        

    def addProdPrice(self,price):
        self.price.append(price)
        
    
    def display(self):
        print("Items Name :- ",self.name)
        print("Items Quantity :- ",self.quantity)
        print("Items Prices($) :- ",self.price)
        


val= inventory()
num=-1
while(num!=0):
    print("<-----1.Add Data 2.Display 3.Update 4.Delete 0.Exit----->")
    num=int(input("Enter the number:-"))
    if(num==1):
        name=input("Enter name :-")
        quantity=int(input("Enter quantity:-"))
        price=int(input("Enter the price:-"))
        val.addProdName(name)
        val.addProdQuantity(quantity)
        val.addProdPrice(price)
        print("--------------------------------------------------")
        
    elif(num==2):
        val.display()
        print("--------------------------------------------------")

    elif(num==3):
        pos=int(input("Enter position to Edit:- "))
        name=input("Enter name :-")
        quantity=int(input("Enter quantity:-"))
        price=int(input("Enter the price:-"))
        val.name[pos-1]=name
        val.quantity[pos-1]=quantity
        val.price[pos-1]=price
        print("--------------------------------------------------")

        
    elif(num==4):
        pos=int(input("Enter position to delete:- "))
        val.name.remove(val.name[pos-1])
        val.quantity.remove(val.quantity[pos-1])
        val.price.remove(val.price[pos-1])
        print("--------------------------------------------------")

    elif (num==0):
        print("Thanku for visiting...")
        exit
    else:
        print("Invalid input...")
        break


