import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(word):
    word = word.lower()
    proper = word.capitalize()
    upper = word.upper()

    if word in data:
        return data[word]
    elif proper in data:
        return data[proper]
    elif upper in data:
        return data[upper]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input('Did you mean %s? Enter "y" for yes and "n" for no: '
                   % get_close_matches(word, data.keys())[0])
        if yn == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'n':
            return 'Re-run the script to find the word you\'re looking for'
        else:
            return 'Invalid query entered'
    else:
        return 'This word cannot be found'


word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for entry in output:
        print(entry)
else:
    print(output)
