from stats import get_num_words
from stats import get_char_count
from stats import sort_char_count
import sys

# Command-line argument check
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Get the book path
book_path = sys.argv[1]

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            file_content = f.read()
            return file_content
    except FileNotFoundError:
        raise Exception(f"The file at '{filepath}' was not found.")
    except PermissionError:
        raise Exception(f"Permission denied for accessing the file at '{filepath}'.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

def main():
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    char_count = get_char_count(book_text)
    sorted_chars = sort_char_count(char_count)

    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for pair in sorted_chars:
        char = pair["char"]
        count = pair["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()
