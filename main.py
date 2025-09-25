def get_book_text(path):
  with open(path) as f:
    file_contents = f.read()
  
  return file_contents

def get_word_count(path):
  with open(path) as f:
    file_contents = f.read()
  file_contents_list = file_contents.split()
  return len(file_contents_list)

def main():
  # print(get_book_text("books/frankenstein.txt"))
  word_count = get_word_count("books/frankenstein.txt")
  print(f"Found {word_count} total words")

main()