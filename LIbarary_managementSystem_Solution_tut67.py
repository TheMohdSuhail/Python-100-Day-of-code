class library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):

        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self.noBooks} books. The books are ")
        for book in self.books:
            print(book)

l1 = library()
l1.addBook("Mohd Suhail 1")
l1.addBook("Hello World")
l1.showInfo()
