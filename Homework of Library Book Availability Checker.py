# Library Book Availability Checker

books = ["Python", "Math", "Science"]
copies = [3, 0, 2]

library = list(zip(books, copies))

# Show available books
available = list(filter(lambda x: x[1] > 0, library))
print("Available Books:", available)

# Update late fees
fees = [2, 3, 4]
new_fees = list(map(lambda x: x + 1, fees))
print("Updated Fees:", list(zip(books, new_fees)))

# Check a book
choice = input("Enter book name: ")

for book, copy in library:
    if choice.lower() == book.lower():
        if copy == 0:
            print("Book unavailable")
            break
        else:
            print("Book available")
            break