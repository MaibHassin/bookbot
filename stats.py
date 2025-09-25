def get_word_count(path):
  with open(path) as f:
    file_contents = f.read()
  file_contents_list = file_contents.split()
  return len(file_contents_list)

def count_chars(path):
  with open(path) as f:
    file_contents = f.read()
  
  char_counts = {}
  for c in file_contents:
    if c.lower() in char_counts:
      char_counts[c.lower()] += 1
    else:
      char_counts[c.lower()] = 1
    
  return char_counts