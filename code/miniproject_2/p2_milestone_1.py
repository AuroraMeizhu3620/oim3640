# loading string and splitting string into list
book = "Before Before Before jumping into code, try sketching your logic in a document or on paper. What steps does your program need to take? What data structures make sense? A few minutes of planning saves hours of debugging."
book = book.split()
print(book)
#file = input("Enter the file name: ") 
#book = open(file).read().split()

# creating dictionary
from pathlib import Path
file_path = Path("data") / "words.txt"
with open(file_path) as f:
    dictionary_words = set(f.read().split())

# identify words in the string
def value_counts(book):
    counter = {}
    for word in book:
        if word in dictionary_words:
            counter[word] = counter.get(word, 0) + 1
    return counter

print(value_counts(book))