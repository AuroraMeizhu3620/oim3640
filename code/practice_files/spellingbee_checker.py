def use_only(word, letters):
    """ Does word use only the allowed letters? 
    >>> use_only("cable", "kcboela")
    True
    >>> use_only("color", "kcboela")
    False
    """
    for letter in word:
        if letter not in letters:
            return False
    return True

def must_use(word, required_letter):
    """Does word have the required letter of the day?
    >>> must_use("cable", "e")
    True
    >>> must_use("color", "e")
    False
    """
    for letter in word:
        if letter == required_letter:
            return True
    return False

def length(word):
    """ Only return words that are more than 4 characters long
    >>> length("cable")
    True
    >>> length("cat")
    False
    """
    if len(word) > 4:
        return True
    return False

def find_words(letters, required_letter):
    """print all valid words."""
    with open("data/words.txt") as word_file:
        for word in word_file:
            word = word.strip()
            if use_only(word, letters) and must_use(word, required_letter) and length(word):
                print(word) 


find_words("kcboela", "e")