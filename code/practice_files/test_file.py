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
         