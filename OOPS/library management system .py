class Book:
    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price

class BookStore:
    def __init__(self):
        self.books = []

    def add_book(self, id, title, price):
        self.books.append(Book(id, title, price))

    def get_book(self, id=None, title=None, price=None):
        for book in self.books:
            if book.id == id or book.title == title or book.price == price:
                return book
        return None

    def show_books(self):
        for book in self.books:
            print(f'ID: {book.id}, Title: {book.title}, Price: {book.price}')

    def delete_book(self, id=None, title=None, price=None):
        self.books = [book for book in self.books if book.id != id and book.title != title and book.price != price]

def main():
    store = BookStore()
    while True:
        print("1. Add book")
        print("2. Get book")
        print("3. Show all books")
        print("4. Delete book")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            id = input("Enter book id: ")
            title = input("Enter book title: ")
            price = float(input("Enter book price: "))
            store.add_book(id, title, price)
        elif choice == 2:
            id = input("Enter book id: ")
            book = store.get_book(id=id)
            if book:
                print(f'ID: {book.id}, Title: {book.title}, Price: {book.price}')
            else:
                print("Book not found")
        elif choice == 3:
            store.show_books()
        elif choice == 4:
            id = input("Enter book id: ")
            store.delete_book(id=id)
        elif choice == 5:
            break

if __name__ == "__main__":
    main()
