# loading string and splitting string into list
book = "Before jumping into code, try sketching your logic in a document or on paper. What steps does your program need to take? What data structures make sense? A few minutes of planning saves hours of debugging."
book = book.split()
print(book)

#file = input("Enter the file name: ") 
#book = open(file).read().split()


# identify words in the string




word_dict = {}
for word in word_list:
    word_dict[word] = 1

def much_faster():
    count = 0
    for word in word_dict:
        if reverse_word(word) in word_dict:
            count += 1
    return count


def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

counter = value_counts('brontosaurus')
counter


delimiter = ' '
t = ['pining', 'for', 'the', 'fjords']
s = delimiter.join(t)
s

string = open('words.txt').read()
len(string)

word_list = string.split()
len(word_list)

'demotic' in word_list

word = 'plumage!'
word = word.strip('!')
word

numbers = {'zero': 0, 'one': 1, 'two': 2}
empty = dict()