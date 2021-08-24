monday_temperatures = [9.1, 8.8, 7.6]

for temperatures in monday_temperatures: #creates a variable temperatures that are inside the data type
    print(round(temperatures))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))
    print("{}: {}".format(key,value))
#to do dictionaries you need to specificy if you are examining items, keys or values in dict

for blooboi in phone_numbers.values():
    print("The phone numbers are %s" % blooboi)

# != means if it is different
x=1 
while x !=10:
    x=x+1
    print(x)

#USE BREAK AND CONTINUE FOR AN EASIER WAY TO BREAK LOOP THAN CONDITIONS

while True:
    username = input('Enter passcode:')
    if username == 'Kevin Fang':
        break
    else:
        continue

