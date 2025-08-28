from stats import get_num_words, get_num_chars, sort_char_counts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    count = get_num_words(book_text)
    char_count = get_num_chars(book_text)
    sorted_counts = sort_char_counts(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char_data in sorted_counts:
        if char_data['char'].isalpha():
            print(f"{char_data['char']}: {char_data['num']}")

main()