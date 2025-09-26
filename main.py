def get_book_text(file_path: str) -> str:
    """Read and return the full text of the book at file_path."""
    with open(file_path, "r") as f:
         contents = f.read()
    return contents 

def count_words(text: str) -> int:
    """Count and return the number of words in the given text."""
    words = text.split()
    return len(words)

def main():
    # Example usage
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()