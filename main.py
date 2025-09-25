from stats import get_word_count

def get_book_text(path):
  with open(path) as f:
    file_contents = f.read()
  
  return file_contents

def main():
  # print(get_book_text("books/frankenstein.txt"))
  word_count = get_word_count("books/frankenstein.txt")
  print(f"Found {word_count} total words")

main()