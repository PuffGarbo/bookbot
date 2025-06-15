from stats import *
import sys

def get_book_text(filepath):
    file_contents = ""
    with open (filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    bookpath = sys.argv[1]
    num_words = word_count(get_book_text(bookpath))
    num_chars = character_count(get_book_text(bookpath))
    sorted_chars = sort_chars(num_chars)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    

main()
