from stats import count_words
from stats import count_characters
from stats import sort_on

sum = 0

def get_book_text(file):
    with open(file, "r", encoding="utf-8") as f:
        file_content = f.read()
    return file_content



def main():

    #print(count_characters(get_book_text("./file.txt")))

    #print(f"the words is {count_words(get_book_text("./file.txt"))}")

    print(sort_on(count_characters(get_book_text("./file.txt"))))

if __name__ == "__main__":
    main()