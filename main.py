def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    character_count = count_characters(file_contents)
    report(word_count, character_count)

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    characters = {}
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def report(word_count, character_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    char_list = []
    for char, count in character_count.items():
        char_list.append({"char": char, "num": count})
    
    char_list.sort(reverse=True, key=sort_on)

    for letter in char_list:
        if letter["char"].isalpha():
            print(f"The '{letter["char"]}' character was found {letter["num"]} times")

    print("--- End report ---")

def sort_on(dict):
    return dict["num"]


main()