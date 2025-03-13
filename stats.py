def count_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_count = {}
    for char in text:
        lowercase = char.lower()
        char_count[lowercase] = char_count.get(lowercase, 0) + 1 
    return char_count

def sort_on(dict):
    return dict["num"]


def get_report(char_count):
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "num": count})
    
    char_list.sort(reverse= True, key=sort_on)
    
    return char_list