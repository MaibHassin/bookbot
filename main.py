import sys
from stats import get_word_count, count_chars, sorted_characters


def get_book_text(path):
  with open(path) as f:
    file_contents = f.read()
  
  return file_contents

def print_report(path, word_count, char_list):
  print("============ BOOKBOT ============")

  print(f"Analyzing book found at {path}...")

  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")

  print("--------- Character Count -------")
  for ch in char_list:
    print(f"{ch['char']}: {ch['num']}")
  print("============= END ===============")

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  path = sys.argv[1]

  total_words = get_word_count(path)

  sorted_list = sorted_characters(count_chars(path))

  print_report(path, total_words, sorted_list)

main()