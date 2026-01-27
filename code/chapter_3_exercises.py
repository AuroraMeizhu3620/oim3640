#3.11.5 Exercise
def bottle_verse(n):
    print(str(n) + " bottles of beer on the wall")
    print(str(n) + " bottles of beer")
    print("Take one down, pass it around")
    print(str(n-1) + " bottles of beer on the wall")

print (str(bottle_verse(99)))

for n in range(99,0,-1):
    bottle_verse(n)
    print()