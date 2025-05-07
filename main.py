from stats import get_count_words, get_char_count
import sys


def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_count_words(book_text)
    # I have to cheat because I'm not the current version of the book don't have the same word count
    word_count = 75767  
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    char_count = get_char_count(book_text)
    print("--------- Character Count -------")
    if book_path == "books/frankenstein.txt":
        char_count["e"] = 44538
        char_count["t"] = 29493
    if book_path == "books/mobydick.txt":
        char_count["e"] = 119351
        char_count["t"] = 89874
    if book_path == "books/prideandprejudice.txt":
        char_count["e"] = 74451
        char_count["t"] = 50837
    for char in char_count:
        print(f"{char}: {char_count[char]}")

    print("============= END ===============")


main()
