def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
        split = file_contents.split()
        letters_list = list(file_contents)

        characters = {}
        
        for letter in letters_list:
            if letter.isalpha() != True:
                continue

            lowercase_letter = letter.lower()
            if lowercase_letter in characters:
                characters[lowercase_letter] += 1
            else:
                characters[lowercase_letter] = 1

        print("--- Begin report of books/frankenstein.txt ---")
        for character in characters:
            print(f"The '{character}' character was found {characters[character]} times")
        print("--- End report ---")
main()
