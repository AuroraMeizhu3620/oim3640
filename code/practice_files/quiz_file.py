# I am using this to check some questions I was confused about in the quiz...
x=5
y=x

def function(x):
    y=x*2
    x=y+1
    return y

print(function(3))
print(x)
print(y)

def triangle(n,character):
    for i in range (n):
        space = " "*(i)
        number = character*(n-i)
        print(space + number)

triangle(5,"#")
         

def count_vowels(s):
    count = 0
    for c in s:
        if c in 'aeiou':
            count += 1
            return count
        return count

print(count_vowels('apple'))