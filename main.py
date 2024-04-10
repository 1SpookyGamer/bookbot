def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text("books/frankenstein.txt")
    print(text)


def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()
main()