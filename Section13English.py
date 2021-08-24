#Making English dictonary json format starts with curly brackets and keys and values
import json

import difflib

data = json.load(open('Texts/dictionary.json')) #makes it into a python dictionary

def load_dictionary(keys): #function calls back the data based on what's typed
    
    if keys.upper() in data:
        upperdata = data[keys.upper()]
        for i in range(len(upperdata)):
            print("{}\n".format(upperdata[i]))
        return ""
    
    keyslower = keys.lower()
    if keyslower in data:
        newdata = data[keyslower]
        for i in range(len(newdata)):
            print("{}\n".format(newdata[i]))
        return ""

    elif keyslower not in data:
        secondary = difflib.get_close_matches(keyslower, data, 2, 0.6)
        if secondary == []:
            return "What kind of gibberish is that???? Try again dipwad."

        enter2= input('Enter Y or N if %s was the word: ' % secondary[0])
        if enter2 == 'Y':
            newdata1 = data[secondary[0]]
            for i in range(len(newdata1)): #how to format for loops with strings --> https://stackoverflow.com/questions/51795644/how-to-print-the-list-in-for-loop-using-format-in-python
                print("%s\n" % newdata1[i])
            return ''

        elif enter2 == 'N': 
            newdata2 = data[secondary[1]]
            if input('Was is this one then: %s? Y or N: ' % secondary[1]) == 'Y':
                for i in range(len(newdata2)):
                    print("%s\n" % newdata2[i])
                return ''
            else:
                return "That was the last possible option. Try another word."

    

enter = input('Enter Word: ')

print(load_dictionary(enter))




