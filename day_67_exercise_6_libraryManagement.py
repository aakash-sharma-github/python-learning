# Day 67
# solution of Library management system
class library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def info(self):
        print(f"Number of books: {self.noBooks}.")
        print("The Books are:")
        for book in self.books:
            print(book)

lib = library()
lib.addBook("Rayamayan")
lib.addBook("Mahabharat")
lib.addBook("Games of Throne")
lib.info()