# syntax to create a new text file and write the contents of an array to it

file = open('writer.txt', 'w')

nums = [1, 2, 3]
for num in nums:
    file.write(str(num) + "\n")

file.close()
