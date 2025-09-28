from stats import get_num_words
from stats import count_each_char   

def get_book_text(file_path: str) -> str:
    """Read and return the full text of the book at file_path."""
    with open(file_path, "r") as f:
         contents = f.read()
    return contents 


def main():
    # Example usage
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)    
    print(f"Found {num_words} total words")
    char_count = count_each_char(book_text)
    print(f"Character counts: {char_count}")
if __name__ == "__main__":
    main()