#Develop a Python program for a basic banking system that handles account transactions. The program should include functionalities for account creation, deposit, withdrawal, and fund transfer. 
# Ensure robust exception handling to manage errors like insufficient balance and invalid inputs. 
# Write the program with concise code and clear error messages for efficient handling of exceptions.


class Bank:
    def __init__(self):
        self.balance=0
        
    def Deposit(self,amount):
        self.balance=self.balance+amount
    
    def Withdrawn(self,amount):
        if(self.balance>amount):
            self.balance=self.balance-amount
        else:
            raise Exception("You do not have amount in the bank...Sorry")
    def FundTranfer(self):
        if(self.balance>amount):
            self.balance=self.balance-amount
            print("Amount Transfer =$",amount)
           
        else:
            raise Exception("You do not have that much amount in bank, Transaction Failed !!!")
        
    def Display(self):
        print("Balance Amount :-$",self.balance)

bank=Bank()


num=-1
while(num!=0):
    print("1.Deposit 2.Withdrawn  3.FundTranfer 4.Display 0.Exit")
    num=int(input("Enter the number:= "))
    if(num==1):
        amount=int(input("Enter the amount to deposit :="))
        bank.Deposit(amount)
    elif(num==2):
        amount=int(input("Enter the amount to Withdrawn :="))
        bank.Withdrawn(amount)
    elif(num==3):
        amount=int(input("Enter the amount to Tranfer :="))
        bank.FundTranfer(amount)
    elif(num==4):
        bank.Display()
    elif(num==0):
        print("Thanku for Visiting.....")
        exit
    else:
        print("Invalid Input from the user..")
