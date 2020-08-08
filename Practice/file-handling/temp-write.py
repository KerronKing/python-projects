# function to convert an array of celcius temps to fahr and write them to a new text file

def temp_converter(temps):
    file = open('temp.txt', 'w')
    for temp in temps:
        if temp > -273.15:
            fahr = temp * 9/5 + 32
            file.write(str(fahr) + '\n')
    file.close()


temp_converter([10, -20, -289, 100])
