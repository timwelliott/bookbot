from stats import get_num_words
from stats import count_each_char   
from stats import create_sorted_list_of_dicts
import sys

def get_book_text(file_path: str) -> str:
    """Read and return the full text of the book at file_path."""
    with open(file_path, "r") as f:
         contents = f.read()
    return contents 


def main():
    # Example usage
        if len(sys.argv) == 2:
            print("============ BOOKBOT ============")
            book_path =  sys.argv[1]
            print(f"Analyzing book found at {book_path}")
            book_text = get_book_text(book_path)
            num_words = get_num_words(book_text) 
            print("----------- Word Count ----------")   
            print(f"Found {num_words} total words")
            char_count = count_each_char(book_text)
            sorted_char_count = create_sorted_list_of_dicts(char_count)
            print("--------- Character Count -------")
            for char_info in sorted_char_count:
                if char_info["char"].isalpha():  # Only print alphabetic characters
                    print(f"{char_info['char']}: {char_info['num']}")
            print("============= END ===============")
        else:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
            
    
if __name__ == "__main__":
    main()