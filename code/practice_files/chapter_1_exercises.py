# 1.9.2 Exercise
round1=round(42.5)
print(round1)
round2=round(43.5)
print(round2)
print("Apparently Python rounds everything to the closest even integer to avoid computing errors. They call this 'rounding fairly.'")

# 1.9.3 Exercise
## Part 1
add_normal=1+1
print(add_normal)
add_positive=1++1
print(add_positive)
add_negative=1+-1
print(add_negative)
print("Both adding a positive number and adding a negative number works.")
print("However, VS Code does highlight the double addition sign. I suppose it is in prevention of redundancy.")
## Part 2
print("You can not leave no operator between two numbers. Python identifies it as a syntax error.")
## Part 3
print("If I leave out the parenthesis when I call a function, Python recgnizes it as a syntax error.")

# 1.9.4 Exercise
print(765)
print('guess: integer')
print(type(765))
print(2.718)
print('guess: floating-point')
print(type(2.718))
print('2 pi')
print('guess: string')
print(type('2 pi'))
print(abs(-7))
print('guess: integer')
print(type(abs(-7)))
print(abs(-7.0))
print('guess: floating-point')
print(type(abs(-7.0)))
print(abs)
print('guess: function')
print(type(abs))
print(int)
print('guess: function')
print(type(int))
print(type)
print('guess: function')
print(type(type))

#1.9.5 Exercise
print('How many seconds are there in 42 minutes 42 seconds?')
seconds = 42*60+42
print(seconds)

print('How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.')
miles = 10/1.61
print(miles)

print('If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?')
average1 = seconds/miles
print(average1)

print('What is your average pace in minutes and seconds per mile?')
average2a = int(average1/60)
average2b = int(average1%60)
print(str(average2a) + 'minutes' + str(average2b) + 'seconds')

print('What is your average speed in miles per hour?')
average3 = average1/3600
print(average3)
