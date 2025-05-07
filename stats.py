def get_count_words(book_text):
    return len(book_text.split())


def get_char_count(text):
    text = text.lower()
    char_freq = {}
    for char in text:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq