import nltk
from nltk.corpus import stopwords
import string
nltk.download('stopwords')

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
        return file_contents
    except FileNotFoundError:
        return "File not found."

def remove_stop_words(string):
    stop_words = set(stopwords.words('english'))
    words = string.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    new_string = ' '.join(filtered_words)
    return new_string

def word_count(str):
    # Create an empty dictionary named 'counts' to store word frequencies.
    counts = dict()
    
    # Split the input string 'str' into a list of words using spaces as separators and store it in the 'words' list.
    words = str.split()

    # Iterate through each word in the 'words' list.
    for word in words:
        # Check if the word is already in the 'counts' dictionary.
        if word in counts:
            # If the word is already in the dictionary, increment its frequency by 1.
            counts[word] += 1
        else:
            # If the word is not in the dictionary, add it to the dictionary with a frequency of 1.
            counts[word] = 1

    # Return the 'counts' dictionary, which contains word frequencies.
    return counts

def remove_punctuation(str):
  no_punct = ""
  for char in str:
    if char not in string.punctuation:
      no_punct = no_punct + char
  return no_punct

# Example usage:
file_path = "paragraphs.txt"  # Replace "example.txt" with the path to your text file
file_contents = read_file(file_path)
# Example usage
filtered = remove_stop_words(file_contents)
filtered = remove_punctuation(filtered)

for freq in word_count(filtered).items():
  print(freq)