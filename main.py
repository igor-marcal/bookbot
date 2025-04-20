import sys
from stats import get_word_count
from stats import get_letter_count
from stats import report

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file = sys.argv[1]
    book_text = get_book_text(file)
    num_words = get_word_count(book_text)
    num_letters = get_letter_count(book_text)
    report(file,num_words,num_letters)

main()