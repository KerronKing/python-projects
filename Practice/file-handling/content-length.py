# The following sequence determines the length of each line (each line is a string) in the opened file

file = open('fruits.txt', 'r')
content = file.readlines()
file.close()
for i in content:
    print(len(i))
