# creating dictionary
from pathlib import Path
file_path = Path("data") / "words.txt"
with open(file_path) as f:
    dictionary_words = set(f.read().split())


# identify the top ten most frequent words in the string
def word_counter(text):
    counter = {}
    words = text.split()
    for word in words:
        clean_word = word.strip(".!?,").lower()
        if clean_word in dictionary_words:
            counter[clean_word] = counter.get(clean_word, 0) + 1
    return counter


def second_element(t):
    return t[1]


# word repetition search
def word_searcher(text, target_word):
    counter = 0
    words = text.split()
    for word in words:
        if word.strip(".!?,").lower() == target_word.lower():
            counter += 1
    return counter


# word sentence retrieval
def word_sentence(text, target_word):
    words = text.split()
    sentences_found = []
    current_sentence = []

    for word in words:
        current_sentence.append(word)

        if word.endswith(".") or word.endswith("!") or word.endswith("?"):
            for w in current_sentence:
                if w.strip(".!?,").lower() == target_word.lower():
                    sentences_found.append(" ".join(current_sentence))
                    break
            current_sentence = []

    return sentences_found


# interactive part
print("Please paste your book into the book.txt file in the data folder")
file_path = Path("data") / "book.txt"
with open(file_path, encoding="utf-8") as f:
    book = f.read()

print("Do you know what key word you are looking for?")
answer_1 = input("Yes or no? ")

if answer_1.lower() == "yes":
    target_word = input("What is the key word you are looking for? ")

    count = word_searcher(book, target_word)
    print(f"\nThe word '{target_word}' appears {count} times in the book.")

    sentences = word_sentence(book, target_word)
    print(f"\nThe sentences containing the word '{target_word}' are:")

    if len(sentences) == 0:
        print("Hmmm.... no sentences were found containing that word.Check whether this word ever appeared in the book.")
    else:
        for sentence in sentences:
            print(sentence)

else:
    print("\nLet's find out the top ten most frequent words in the book!")
    items = sorted(word_counter(book).items(), key=second_element, reverse=True)

    if len(items) == 0:
        print("Is this book meant for humans? No dictionary words were found.")
    else:
        print("\nTop ten most frequent words:")
        for word, freq in items[:10]:
            print(freq, word, sep="\t")

        print("\nNow you can choose one of these words to search for in sentences.")
        target_word = input("Enter one word from the list: ")

        count = word_searcher(book, target_word)
        print(f"\nThe word '{target_word}' appears {count} times in the book.")

        sentences = word_sentence(book, target_word)
        print(f"\nThe sentences containing the word '{target_word}' are:")

        if len(sentences) == 0:
            print("No sentences were found containing that word.")
        else:
            for sentence in sentences:
                print(sentence)