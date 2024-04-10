def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text("books/frankenstein.txt")
    count = count_words("books/frankenstein.txt")
    alphabet=letter_count("books/frankenstein.txt")
    print(text)
    print(len(count))
    print(alphabet)
    for key in alphabet.keys():
        print(key, ":", alphabet[key])



def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def count_words(path):
    
    with open("books/frankenstein.txt") as f:
        book=f.read()
        mycount=book.split()
        return mycount

def letter_count(path):
    with open("books/frankenstein.txt") as f:
        book=f.read()
        lowers=book.lower()
        res={}
        for keys in book:
            res[keys]=res.get(keys,0)+1
    return res


main()