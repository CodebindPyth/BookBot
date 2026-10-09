dict1_dict = {}

def count_words(file_content):
    words = file_content.split()
    pap = len(words)
    return pap

def count_characters(file_content):
    lower1 = file_content.lower()
    dict1_count = {}

    for y in lower1:
        dict1_count[y] = lower1.count(y)

    return dict1_count

def sort_on(dict1_count):
    sorted_dict = dict(sorted(dict1_count.items(), key=lambda kv: kv[1]))
    return sorted_dict

