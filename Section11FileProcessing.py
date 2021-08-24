myfile= open("fruits.txt") #opens file
#print(myfile.read()) #reads and prints out the file

#the cursor reads from line 1 to 6, so in order to run a file/txt multiple times you ened to set it equal to a varaible
content=myfile.read()

myfile.close() #closes the file (helps with RAM processing speed)

print(content,content)

with open("fruits.txt") as fruity: #does all that above in one line.
    fruityread=fruity.read()
#inside these with to open these things we do not need a .close
print(fruityread)

with open("Texts/fruits2.txt","r") as fresh:
    freshread=fresh.read()
#must specifcy folder location if script and file aren't in same place


with open("Texts/morefruits.txt","w") as morefruitys:
    morefruitys.write("eggplant \ngrapes \ndeez nuts")
#use "r" for reading and "w" for writing and adding/creating a new file

#in help('open') theres a lot of different modes to write in
#use "a" for adding to existing files or "x" to make new file and write

with open("Texts/morefruits.txt","a") as nextlevel:
    nextlevel.write("\ngarlic\noh wait that's not a fruit")

with open("Texts/morefruits.txt","a+") as lastlevel:
    lastlevel.write("\njello doctor")
    lastlevel.seek(0)
    content=lastlevel.read()

print(content)

