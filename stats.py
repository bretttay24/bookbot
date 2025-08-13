# This function will return the word count

def booktext_wordcount(text_string):    # This takes a string text argument 
    split_text = text_string.split()
    word_count = len(split_text)

    return word_count



# This function will give character count of each character in the text in a diction. {'t': 29493, 'h': 19176, etc..}

def specific_character_count(text_string):    # This takes a string text arguement 
    lower_case_text = text_string.lower()
    char_count_dict = {}
    for character in lower_case_text:
        if character in char_count_dict:
            char_count_dict[character] +=1   # this updates key:value pair  (character: value+1)
        else:
            char_count_dict[character] = 1   # this creates a key:value pair (character: 1) setting 1 as the initial value
    return char_count_dict


# This function will create a structured report of the text
def sort_on(dictionary):
    return dictionary["num"]

def sorted_list_from_dictionary(character_dictionary):
    dictionary_list = []
    for key in character_dictionary:
        new_dictionary = {}
        new_dictionary["char"]= key
        new_dictionary["num"]= character_dictionary[key]
        dictionary_list.append(new_dictionary)

    dictionary_list.sort(reverse=True, key=sort_on)

    return dictionary_list #sorted_dict_list







