class Library():
    def __init__(self,bl=None):
        self.bl=bl
        self.lenddict={}
        

        if(bl is None):
            self.bl=[]
        else:
            self.bl=bl

    def displaybooks(self):
        print(f"we have following books in our library")
        
        for book in self.bl:
            print(book)
       

    def Lendbook(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("lender-book database has been updated")
            print("lenders list = ",self.lenddict)

        else:
            print("book is available you can have it,Thankyou...")

    def addbook(self,book):
        self.bl.append(book)
        print("book has been added to the booklist")
        print(self.bl)

    def returnBook(self,book):
        self.lenddict.pop(book)
        print(self.lenddict)





vamshi=Library(['java','c','c++','python'])

if __name__=='__main__':
   
   while(True):
        print(f"Welcome to the library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        userchoice=int(input("enter from the above following : "))

        if (userchoice==1):
            vamshi.displaybooks()
            bookchoice=input("enter the book name you want : ")
            print('thank you will deliver it soon')

            
        elif (userchoice==2):
            book=input("enter the book name you want to lend : ")
            user=input("enter your name : ")
            vamshi.Lendbook(user,book)


        elif (userchoice==3):
            book=input("enter the book name you want to add : ")
            vamshi.addbook(book)

        elif (userchoice==4):
            book=input("enter the book name you want to return : ")
            print("Remaining lenders list is below")
            vamshi.returnBook(book)

        else:
            print("Not a valid option")

        print("press q to quit or c to continue")
        userchoice2=input()
        if(userchoice2=='q'):
            exit()
        elif (userchoice2=='c'):
            continue

