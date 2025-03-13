import sys
from stats import count_words, character_count, get_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    book_text = get_book_text(file_path)
    num_words = count_words(book_text)
    char_count_dict = character_count(book_text)
    sorted_char_list = get_report(char_count_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_char_list:
        char = char_dict["char"]
        count = char_dict["num"] 
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

main()