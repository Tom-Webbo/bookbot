def main():
    book = "books/frankenstein.txt"
    count = {}
    counter = 0
    with open(book) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        words = file_contents.split()
        for word in words:
            counter += 1
            for letter in word:
                if letter in count:
                    count[letter] += 1
                else:
                    count[letter] = 1
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{counter} words found in the document")
    for k in count:
        print(f"the {k} character was found {count[k]} times")


main()