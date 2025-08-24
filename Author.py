class Author:
    def __init__(self,name,books=[]):
        self.name=name
        self.books=books
    def add_book(self,book):
        self.books.append(book)
    def display(self):
        print(f"Author name={self.name}")
        for book in self.books:
            print(f"{book.title},{book.publication_year}")
class Book:
    def __init__(self,title,publication_year):
        self.title=title
        self.publication_year=publication_year
Author1=Author("Rabindranath Tagore")
book1=Book('dui bigha jami',1920)
book2=Book('Gitanjali',1905)
Author1.add_book(book1)
Author1.add_book(book2)
Author1.display()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     