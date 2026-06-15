class Author:
    # Keep a record of every author created in this project.
    all = []

    def __init__(self, name):
        # Store the author name and register the new author globally.
        self.name = name
        Author.all.append(self)

    def contracts(self):
        # Return all contracts associated with this author.
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        # Return the books connected to this author through contracts.
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        # Create a new contract between this author and the given book.
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # Add up all royalties earned by this author across contracts.
        return sum(contract.royalties for contract in self.contracts())


class Book:
    # Keep a record of every book created in this project.
    all = []

    def __init__(self, title):
        # Store the title and register the new book globally.
        self.title = title
        Book.all.append(self)

    def contracts(self):
        # Return all contracts linked to this book.
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # Return the authors connected to this book through contracts.
        return [contract.author for contract in self.contracts()]


class Contract:
    # Keep a record of every contract created in this project.
    all = []

    def __init__(self, author, book, date, royalties):
        # Validate each field before storing the contract.
        self.author = self._validate_author(author)
        self.book = self._validate_book(book)
        self.date = self._validate_date(date)
        self.royalties = self._validate_royalties(royalties)
        # Register the contract in the global collection.
        Contract.all.append(self)

    @staticmethod
    def _validate_author(author):
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance")
        return author

    @staticmethod
    def _validate_book(book):
        if not isinstance(book, Book):
            raise Exception("Book must be a Book instance")
        return book

    @staticmethod
    def _validate_date(date):
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        return date

    @staticmethod
    def _validate_royalties(royalties):
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        return royalties

    @classmethod
    def contracts_by_date(cls, date):
        # Return every contract that matches the provided date.
        return [contract for contract in cls.all if contract.date == date]