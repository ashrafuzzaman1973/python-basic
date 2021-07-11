#stack is last-in first-out (LIFO)
books = []
books.append("learn c")
books.append("learn c++")
books.append("learn java")
books.pop()
print(books)
print("Now the top book is :",books[-1])

books.pop()
print(books)
print("Now the top book is :",books[-1])

books.pop()
if not books:
    print("No books left")