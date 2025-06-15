def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_count = {}
    for c in text:
        char = c.lower()
        if (char in char_count):
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(keys):
    return keys["num"]

def sort_chars(chars):
    sorted_chars = []
    for char in chars:
        sorted_chars.append({"char": char, "num": chars[char]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars


