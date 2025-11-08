from stats import total_word_count,word_counter,convert_to_list
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    count = total_word_count(text)
    print(f"Found {count} total words")
    word_dict = word_counter(text)
    #print(word_dict)
    sorted_list = convert_to_list(word_dict)
    for entry in sorted_list:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()