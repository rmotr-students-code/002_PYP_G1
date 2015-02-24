class Programming(object):
    
    def __init__(self, title, book_id, subject):
        self.title = title
        self.book_id = book_id
        self.subject = subject
    

class Textbook(object):
    
    def __init__(self, title, book_id, *genre):
        self.title = title
        self.book_id = book_id
        self.genre = [g for g in genre]
    
    # special method
    def __le__(self, another_book):
        return self.book_id <= another_book.book_id
    
    # def __str__(self):
    #     return "{}".format(format_book(self.title))
        
    # def __unicode__(self):
    #     return "{}".format(format_book(self.title))
    
    @property
    def tags(self):
        all_tags = [tag.lower() for tag in self.genre]
        return all_tags

    @staticmethod
    def format_book(book_title):
        return book_title.capitalize


    @classmethod
    def submit_books(cls, all_books):
        bookshelf = []
        for title, book_id, genre in all_books:
            add_book = cls(title, book_id, genre)
            bookshelf.append(add_book)
        return bookshelf

books_to_add = [
        ("Introduction to Algorithms CLSR", 1, "math"),
        ("Cracking the Code Interview", 2, "interview"),
        ("The Pragmatic Programmer", 3, "developer")
    ]
books = Textbook.submit_books(books_to_add)

for book in books:
    print(book)
    
class ProgrammingTextBook(Programming, Textbook):
    pass

intro_to_programming = ProgrammingTextBook("coding101", 101, "python")

print(intro_to_programming.subject)