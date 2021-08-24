#int (converts a value into an integer [can't convert things like Hello])
#str converts to string
#modules cntains functions use import {function} i.e math
#dot notation allows to access one of the functions, need to specificy name of module and function
#i.e decibels=10*math.log(variable)
#height=math.sin(variable)
#def defines a function --> def print_lyrics(): [empty parenthesis doesn't take arguments]
#to end a function you need to have an empty line
#to call it, just type the function

#def print_lyrics():
    #print ("I'm a lumberjack, and I'm okay.")
    #print ('I sleep all ngiht and I work all day.')

#def repeat_lyrics():
    #print_lyrics()
    #print_lyrics()

#repeat_lyrics()

#def print_twice(bruce):
#the arguments are assigned to variables called parameters

def print_twice(bruce):
    print (bruce)
    print (bruce)
#import math
#pi=math.pi
#print(pi)

print_twice('Spam')
#print_twice(17)
#print_twice(pi)

#when you create a variable inside a function, it is local, which means it only exists inside function

def cat_twice(part1, part2):
    cat= part1 + part2
    print_twice(cat)

line1= 'Bing tiddle'
line2= ' tiddle bang.'
#cat_twice(line1, line2)

#list of functions in an NamError is a traceback, tells you what program file the error occured, and what line
#fruitful functions: things like math functions
#void functions: functions like the print_twice or cat_twice

#from math import pi (import an object from a module)
#from math import * (imports everyhing from the module)

def right_justify(allen):
    x=' '
    print(70*x +allen)

print(right_justify('deez nuts'))

import datetime
lol=datetime.datetime.now()
print("The date and time is",lol)
#in split terminals make one with >>> a python shell by typing python
#to run a script run in the > terminal by typing python "filename".py