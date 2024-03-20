class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if type(name) is not str:
            raise Exception
        self._name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        total = 0
        get_royalties = [contract.royalties for contract in Contract.all if contract.author == self]
        for r in get_royalties:
            total += r
        return total

class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if type(title) is not str:
            raise Exception
        self._title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception
        self._author = author

    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise Exception
        self._book = book

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, date):
        if type(date) is not str:
            raise Exception
        self._date = date
    
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self, royalties):
        if type(royalties) is not int:
            raise Exception
        self._royalties = royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]