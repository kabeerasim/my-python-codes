
from datetime import datetime
from os import O_EXCL, remove
from types import new_class

current_time = datetime.now()


class Library:
    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.lended_book = {}
    
    @property
    def display(self):
        print(f"Here are all of the books that are available to {self.library_name}")
        for book in self.list_of_books:
            print(book)


    def lend(self, user, book):
        if book not in self.lended_book.keys():
            self.lended_book.update({book:user})
            self.list_of_books.remove(book)
            print("Your request has been approved")
            with open("logs.txt", "a") as f:
                f.write(f"{book}. This book is given to our customer at {current_time}\n")
        else:
            print(f"Book is already being used by {self.lended_book[book]}")
         
    def donate(self, donated_book):
        self.list_of_books.append(donated_book)
        print(f"Thank you for donating {donated_book} to us.")
        with open("logs.txt", "a") as f:
            f.write(f"'{donated_book}' This book is donated to us at {current_time}\n")

    
    def returning(self, returned_book):
        if returned_book in self.lended_book.keys():
            print(f"Thank you for returning '{returned_book}' to us")
            with open("logs.txt", "a") as f:
                f.write(f"'{returned_book}' This book is returned to us at {current_time}\n")
            self.lended_book.pop(returned_book)
        elif returned_book in self.list_of_books:
            print("This book is already been returned to us. :)")
        else:
            print(f"This book is not ours. :)")
        

    
if __name__ == '__main__':
    MyLibrary = Library(["Notes on an Execution", "To a Paradise", "Young Mungo", "Whala: A Novel", "Lost & Found"] , "MyLibrary")
    while True:
        

        print("\nThis is a Library Management System.  ")
        userinput = str(input("Choose your prefered option:\n1. Display all the books that are available\n2. Lend you a book if that is available\n3. Donate a book to us\n4. Return a book to us\n"))

        listb = ["Notes on an Execution", "To a Paradise", "Young Mungo", "Whala: A Novel", "Lost & Found"]

        if userinput == "1":
            MyLibrary.display
        elif userinput == "2":
            book = input(f"Which book you want to lend?\n{MyLibrary.list_of_books} Type the exact name.\n")   
            if book in MyLibrary.list_of_books or book in MyLibrary.lended_book:
                user = input(f"Please Enter Your Name:\n")
                MyLibrary.lend(user, book)
            else:
                print("Sorry we do not have this book")


        elif userinput == "3":
            donated_book = input("Please enter the name of the book you want to donate to us\n")
            MyLibrary.donate(donated_book)
            
        elif userinput == "4":
            returninput = input("Which of our book you want to return\n")
            returned_book = returninput 
            MyLibrary.returning(returned_book)
        else:
            print("What the hell is this?") 

        print("Press q to quit and c to continue")
        user_choice =  ""
        while(user_choice!="c" and user_choice!="q"):
            user_choice = input()
            if user_choice == "q":
                exit()

            if user_choice == "c":
                continue        

        


                
                

            


