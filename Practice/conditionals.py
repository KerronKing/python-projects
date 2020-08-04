def converter(deg):  # Function to convert celcius to fahrenheit
    if deg < -273.15:
        return 'Conversion not possible'
    else:
        fahr = (deg * 9/5) + 32
        return fahr


print(converter(32))
print(converter(-272))


def str_length(word):  # Function to return the length of a string
    if type(word) == int:
        return 'Sorry, integers don\'t have length'
    elif type(word) == float:
        return 'Sorry, floats don\'t have length'
    else:
        return len(word)


print(str_length('kerron'))
print(str_length(1))
print(str_length(1.2))
