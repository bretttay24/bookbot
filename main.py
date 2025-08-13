from stats import booktext_wordcount, specific_character_count, sorted_list_from_dictionary  #import functions from stats.py
import sys


if len(sys.argv) != 2:
    message = """ 
    When using Command line call main.py and book.txt you want from the books directory.
    Format CLI Usage: python3 main.py <path_to_book>
    example: python3 main.py books/frankenstein.txt
    """
    print(message)
    sys.exit(1)

file_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        file_text = file.read()
        
        return file_text

def main():
    book_text = get_book_text(file_path)
    word_count = booktext_wordcount(book_text)
    character_count_dictionary = specific_character_count(book_text)
    sort_dict_list = sorted_list_from_dictionary(character_count_dictionary)
   
    report_header = f"""
    ============ BOOKBOT ============
    Analyzing book found at {file_path}
    ----------- Word Count ----------
    Found {word_count} total words
    --------- Character Count -------
    """

    report_tail= "============= END ==============="

    print(report_header)
    # This portion will be under
    # "--------- Character Count -------"
    for dictionary in sort_dict_list:
        key = dictionary["char"]
        value = dictionary["num"]
        if key.isalpha() == True:
            print(f"\n {key}: {value}")
        else:
            continue

    print(report_tail)
    #"report_tail= "============= END ===============""
main()

