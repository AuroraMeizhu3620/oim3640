# Read entire file
with open('data/s20.txt') as f:
    text = f.readline() # read line by line in large files
    print(text)

# Read line by line
with open('data/s20.txt') as f:
    for line in f:
        print(line.strip()) #strip() removes \n
    
# Write to file ('w' = overwrite, 'a' = append)
with open('data/s20_output.txt', 'w') as f: #w is overwrite, a is append
    f.write('Hello, World!\n')