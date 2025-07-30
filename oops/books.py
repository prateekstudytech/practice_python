# Basic Class Definitions

class Book:
    def __init__(self, title: str, author: str, pages: int, price: float):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is secret attribute"
    
    def get_price(self):
        if hasattr(self, "_discount"):
            return (self.price - (self.price*self._discount))
        else:
            return self.price

    def set_discount(self, percent):
        self._discount = percent/100


class Newspaper:
    def __init__(self):
        self.name = name

if __name__ == "__main__":
    book1 = Book("War of the Worlds", "H. G. Wells", 310, 30.01)
    book2 = Book("War and Peace", "Leo Tolstoy", 642, 40 )

    # print(book1.title, book1.author, book1.price)
    # book2.set_discount(50)
    # print(book2.title, book2.author, book2.get_price())
    
    print(book2._Book__secret)

    print(isinstance(book1, Book))
    
