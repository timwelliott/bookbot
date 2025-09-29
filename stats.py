def get_num_words(text: str) -> int:  
    """Count and return the number of words in the given text."""
    words = text.split()
    return len(words)

def count_each_char(text: str) -> dict:
    """Count occurrences of each character in the text and return as a dictionary."""
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_num_from_dict(data: dict) -> int:
    """Return data["num"]."""
    return data["num"]

def create_sorted_list_of_dicts(data: dict) -> list:
    """Convert a dictionary to a sorted list of dictionaries with 'char' and 'num' keys."""
    list_of_dicts = [{"char": char, "num": num} for char, num in data.items()]
    list_of_dicts  = sorted(list_of_dicts, key=get_num_from_dict, reverse=True)
    return list_of_dicts