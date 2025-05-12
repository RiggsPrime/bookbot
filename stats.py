def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_char(text):
    lowercase_text = text.lower()
    chars = list(lowercase_text)
    char_dic = {}

    for char in chars:
        # add char to dictionary if it's not there. Otherwise, increment char's count value by 1
        if char not in char_dic:
            char_dic.update({char: 1})
        else:
            char_dic[char] += 1
    return char_dic
            
def sort_chars(char_dictionary):
    sorted_char_list = []
    # This is a way of converting dictionaries to lists, using the 'lambda' function.
    sorted_char_dict = dict(sorted(char_dictionary.items(), reverse=True, key=lambda item: item[1]))

    for char in sorted_char_dict:
        if char.isalpha():
            sorted_char_list.append(f"{char}: {sorted_char_dict[char]}")
        sorted_char_str = "\n".join(sorted_char_list)
    return sorted_char_str
