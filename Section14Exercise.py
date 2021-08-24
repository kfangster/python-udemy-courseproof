import mysql.connector

import time

import difflib #now gonna combine the previous parts of Section 13 instead of using import json to open data

import numpy #np.array for this tuple/list issue

con = mysql.connector.connect(
user = 'ardit700_student',
password = 'ardit700_student',
host = '108.167.140.122',
database = 'ardit700_pm1database' 
)

cursor = con.cursor()

Dictionary = cursor.execute("SELECT * FROM Dictionary")

results = cursor.fetchall() 

new_dictionary = []
expression = []
definition = []

#results = numpy.array(results)

for i in range(len(results)):
    new_addition = results[i]
    expression.append(new_addition[0])
    definition.append(new_addition[1:])

#next goal: somehow have the words with multiple definitions become 1 term in list, and not multiple!!!! <------

print('hello')


#results is a list, but unorganized. to organize: use for loop with if else statements to combine correct term and defs

#when calling the parts from the results, it's a tuple. so must use list(tuple) to append the other defs onto it.

#convert list into a dictionary of sorts to use get_close_matches
#use same function method for all capital and lowercase letters too!





#enterword = input('Enter word: ')

#query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % enterword)

#results_secondary = cursor.fetchall()

#def dictionaryfinder(word):
    #if enterword not in results:
        #other_words = difflib.get_close_matches(enterword, results, 2, 0.6)
        #print(other_words)


#for i in range(len(results)):
    #new_result = results[i]
    #time.sleep(2)
    #print(new_result[1])
    #print('')