def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        #print(file_contents)
        print('--- Begin report of books/frankenstein.txt ---')
        print(f'{words(file_contents)} words found in the document\n')
        char_list = characters(file_contents)
        for character in char_list:   
            print(f"The '{ character['letter']}' character was found {character['frequency']} times")
        print('--- End report ---')

def words(book):
    book = str(book)
    word_list = book.split()
    return len(word_list)

def characters(book):
    book = book.lower()
    character_dictionary = {}
    for char in book:
        if char == ' ':
            continue
        elif char not in character_dictionary:
            character_dictionary[char] = 1
        else:
            character_dictionary[char] += 1

    alpha_list = []
    for key in character_dictionary:
        if key.isalpha():
            alpha_list.append({'letter':key,'frequency': character_dictionary[key]})
    
    
    alpha_list.sort(reverse=True,key=sort_on)

    return alpha_list

def sort_on(dict):
    return dict["frequency"]

main()