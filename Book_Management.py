
#Problem3-Create a Python program for a simple bookstore inventory system. Using lists and tuples, store book details like title, author, and price. 
# Allow users to add new books and update prices. Provide the option to search for books by title or author.




class bookstore:
    def __init__(self):
        self.title=[]
        self.author=[]
        self.price=[]

    def addData(self,title,author,price):
        self.title.append(title)
        self.author.append(author)
        self.price.append(price)
        
    def display(self):
        print("Book Name :- ",self.title)
        print("Author Name :- ",self.author)
        print("Book Prices($) :- ",self.price)
        


val= bookstore()
num=-1
while(num!=0):
    print("<-----1.Add Data 2.Display 3.Update 4.Delete 5.Search 0.Exit----->")
    num=int(input("Enter the number:-"))
    if(num==1):
        title=input("Enter Title :-")
        author=input("Author Name:-")
        price=int(input("Enter the price:-"))
        val.addData(title,author,price)
        print("--------------------------------------------------")
        
    elif(num==2):
        val.display()
        print("--------------------------------------------------")

    elif(num==3):
        pos=int(input("Enter position to Edit:- "))
        title=input("Enter Title :-")
        author=input("Author Name:-")
        price=int(input("Enter the price:-"))
        val.title[pos-1]=title
        val.author[pos-1]=author
        val.price[pos-1]=price
        print("--------------------------------------------------")

        
    elif(num==4):
        pos=int(input("Enter position to delete:- "))
        val.title.remove(val.title[pos-1])
        val.author.remove(val.author[pos-1])
        val.price.remove(val.price[pos-1])
        print("--------------------------------------------------")
    elif(num==5):
        search=input("Enter the book you want to search :- ")
        if search in val.title:
            print("Yes !!! Book exist in the library.")
        else:
            print("Sorry !!! No book matched in the library.")

    elif (num==0):
        print("Thanku for visiting...")
        exit
    else:
        print("Invalid input...")
        break


