# function that iterates over a list and print each element
def print_list(myList):
    for item in myList:
        print(item)


print_list([1, 2, 3, 4, 5])


# function that iterate over a list and prints all elements greater than 2
def print_over_two(myList):
    for item in myList:
        if item > 2:
            print(item)


print_over_two([1, 2, 3, 4, 5])


# function that converts the temperatures in a list from celcius to fahrenheit
def temp_converter(myList):
    for item in myList:
        if item < -273.15:
            print('This number cannot be converted')
        else:
            print(item * 9/5) + 32


temp_converter([10, -20, -289, 100])
