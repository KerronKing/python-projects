# The following opens, reads, closes and prints the contents of a file

file = open("fruits.txt", "r")
content = file.read()
file.close()

print(content)
