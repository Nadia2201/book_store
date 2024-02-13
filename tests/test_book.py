from lib.book import Book

def test_book_constructs():
    book = Book(1, "Nineteen Eighty-Four", "George Orwell")
    assert book.id == 1
    assert book.title == "Nineteen Eighty-Four"
    assert book.author_name == "George Orwell"
def test_book_format_nicely():
    book = Book(1, "Test title", "Test author")
    assert str(book) == "Book(1, Test title, Test author)"
def test_books_are_equal():
    book1 = Book(1, "Test Book", "Test Author")
    book2 = Book(1, "Test Book", "Test Author")
    assert book1 == book2