'''
Q. Write a Library class with no_of_books and books as two instance variables.
Write a program to create a library form this Library class and show how you can print
all books, and get the number of books using different methods Show that your porgram
doesnt persist the books after the program is stopped!



'''

class library:
    

    def __init__(self):
        book = []
        

        while True:

            check = int(input("Enter 1 for Add Book and 0 for exit\n"))
            if (check == 1):
                
                a = input("Enter Book Name \n")
                book.append(a)

            elif(check == 0):
                break
        print(book)

        no_of_books = len(book)
        print(no_of_books)

obj = library()
