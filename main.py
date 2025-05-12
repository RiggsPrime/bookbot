from stats import count_words
from stats import count_char
from stats import sort_chars
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_char = count_char(book_text)
    sorted_chars = sort_chars(num_char)
    print(sorted_chars)
    print("============= END ===============")
    
main()
