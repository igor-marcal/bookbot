def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letter_count = {}
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter in letter_count:
            letter_count[lower_letter] +=1
        else:
            letter_count[lower_letter] =1
    return letter_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def report(book_file, num_words, letter_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in letter_count:
        print(f"{letter}: {letter_count[letter]}")
    print("============= END ===============")