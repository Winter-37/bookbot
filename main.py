def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(file_contents)
        print(words(file_contents))

def words(book):
    book = str(book)
    word_list = book.split()
    return len(word_list)


main()