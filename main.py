def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        return file_contents

def count_numbers(file_as_string):
    return len(file_as_string.split())

def count_letters(file_as_string):
    words = file_as_string.lower().split()
    dictionary = {}
    for word in words:
        worldList = list(word)
        for ch in worldList:
            if ch in dictionary.keys():
                dictionary[ch] += 1
            else:
                dictionary[ch] = 1
    return dictionary

def print_words(dictionary):
    for x in dictionary:
        print("The '", x, "' character was found ", dictionary[x], "times")

def print_report():
    print('--- Begin report of books/frankenstein.txt ---')
    print(count_numbers(main()), 'words found in the document')
    print_words(count_letters(main()))

print_report()