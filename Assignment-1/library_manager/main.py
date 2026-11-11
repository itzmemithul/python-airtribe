from models import Book, LibraryItem, Member, Magazine, DVD  # TODO: also import Magazine, DVD
book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Today", 2, 45)
dvd = DVD("Inception", 3, 148)
book2 = Book("Deep Learning", 4, "Ian Goodfellow")

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# abstract checkpoint
try:
    LibraryItem("x", 1)
except TypeError as e:
    print("Cannot create LibraryItem", e)

# same item twice
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

# borrow limit of 1 for bob
try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)  # should fail: limit reached
except ValueError as e:
    print("Could not borrow:", e)

# Alice default limit of 3 items
try:
    alice.borrow(dvd)
    alice.borrow(book2)
    extra = Book("Hands-on-LLMs", 5, "Jay Almar")
    alice.borrow(extra)
except ValueError as e:
    print("Could not borrow:", e)

# not borrowed
try:
    alice.return_item(dvd)
except ValueError as e:
    print("Could not return:", e)

# Polymorphism: one loop, no type checks
items = [book, magazine, dvd]  # TODO: add the magazine and the DVD
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))
# Class attribute shared by all objects
print("Total items created:", Book.total_items)

# Encapsulation: private list of borrowed items
try:
    print(book.__available)
except AttributeError as e:
    print("Cannot access private attribute:", e)
print("Available via getter:", book.is_available())