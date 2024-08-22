"""
BookBot

Boot.dev Guided Project for learning python (may contain bad code)

Functions:
    main: entrypoint to the project
    book_word_count: takes in text and returns wordcount
    character_counter: takes in text and returns no. times character appears
    print_report: print a report on the occurrences of a character
    convert_dict: takes in a compounded dictionary and return a list of dictionaries
    sort_dict: takes in the book dictionary and sorts it by the value

Usage:
    You run it.. see what happens
"""


def main():
    """
    Main entry point of the project
    """

    with open("./books/frankenstein.txt", "r", encoding="utf-8") as f:
        file_contents = f.read()

        # count the number of words in the text
        word_count = book_word_count(file_contents)

        # count the number of characters
        char_count = character_counter(file_contents)

        # convert char_count to list
        dict_list = convert_dict(char_count)

        # sort the dictionary
        dict_list.sort(reverse=True, key=sort_dict)

        # print the report
        print_report(word_count, dict_list)


def book_word_count(text: str):
    """
    takes in text and returns the word count
    """

    words = text.split()
    return len(words)


def character_counter(text: str):
    """
    takes in text, and counts how many times characters appeared in it
    """

    char_count = {}
    lowercase = text.lower()
    for l in lowercase:
        if l in char_count:
            char_count[l] += 1
            continue
        char_count[l] = 1
    return char_count


def convert_dict(table: dict[str, int]):
    """
    takes in text, and counts how many times characters appeared in it
    """

    char_list = [{"key": key, "value": value} for key, value in table.items()]
    return char_list


def sort_dict(table):
    """
    takes in text, and counts how many times characters appeared in it
    """

    return table["value"]


def print_report(word_count: int, dict_list: list):
    """
    takes in text, and counts how many times characters appeared in it
    """

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    for d in dict_list:
        if d["key"].isalpha():
            print(f"The '{d['key']}' was found {d['value']} times")


main()
