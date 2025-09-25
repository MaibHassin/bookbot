def get_word_count(path):
  with open(path) as f:
    file_contents = f.read()
  file_contents_list = file_contents.split()
  return len(file_contents_list)