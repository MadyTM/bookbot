from stats import get_num_words, get_num_chars, sort_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    count = get_num_words(book_text)
    char_count = get_num_chars(book_text)
    sorted_counts = sort_char_counts(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char_data in sorted_counts:
        if char_data['char'].isalpha():
            print(f"{char_data['char']}: {char_data['num']}")

main()