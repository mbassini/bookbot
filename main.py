def main():
    print("--- Begin report of books/frankenstein.txt ---")

    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as file:
        content = file.read()
        
        words_count = count_words(content)
        print(f"{words_count} words found in the document")
        print()

        chars_counter = count_chars(content)
        chars_counter_list = convert_dic_to_list(chars_counter)
        chars_sorted = sort_by_count(chars_counter_list)

        for char in chars_sorted:
            if char["value"].isalpha():
                print(f"The '{char["value"]}' was found {char["count"]} times")

        print()
        print("--- End report ---")
        


def count_words(text):
    words_list = text.split()
    return len(words_list)

def count_chars(text):
    chars_counter = {}

    for char in text:
        char = char.lower()
        if char in chars_counter:
            chars_counter[char] += 1
        else:
            chars_counter[char] = 0

    return chars_counter

def convert_dic_to_list(chars_counter):
    list_of_dics = []

    for key in chars_counter:
        dic = {}

        dic["value"] = key
        dic["count"] = chars_counter[key]

        list_of_dics.append(dic)

    return list_of_dics

def sort_by_count(counter_list):
    counter_list.sort(reverse=True, key=sort_on)
    return counter_list
    
def sort_on(dict):
    return dict["count"]

main()
