def total_word_count(text) -> int:
    words = text.split()
    count = 0
    for word in words:
        count +=1
    return count

def word_counter(text) -> dict:
    word_dict = {}
    count = 0
    for word in text:
        word = word.lower()
        if word in word_dict:
            word_dict[word]+=1
            continue
        word_dict[word]=1
    return word_dict


def convert_to_list(word_dict):
    word_list = []
    for word in word_dict:
        word_list.append({"char":word,"num":word_dict[word]})
    word_list.sort(reverse=True,key=sort_on)  
    return word_list

def sort_on(word_dict):
    return word_dict["num"]
