class Books(object):

    def __init__(self, books):
        self.books = books

    def count_books(self):
        print(f"I have {len(self.books)} books!")

        print("They are:")
        for book in self.books:
            print(book)


my_books = Books(["Learn python the hard way",
                  'Little prince',
                  'Happy farmer'])

your_books = Books(["Harry potter 1",
                    "Harry potter 2",
                    "Harry potter 3",
                    "Harry potter 4"])

my_books.count_books()
your_books.count_books()
