import time #time module

import os #os module  

import pandas #pandas used for data analysis

#remember if stuck use dir('') and help('') to your advantage

while True:
    if os.path.exists('Texts/fruits3.txt'): #returns a True false statement for a file if it exists or not
        with open("Texts/fruits2.txt",'r') as file_name:
            time.sleep(3)
            print(file_name.read())
    else:
        print('File does not exist')
        break

while True:
    if os.path.exists('Texts/stats.csv'):
        data = pandas.read_csv("Texts/stats.csv")
        print(data.mean())
        time.sleep(10)
    else:
        print('File does not exist')
        break




  