#Component data types: list most popular one
#i.e x= [9.1,3,4]
x=list(range(1,20,2))
#print(x)

#in python terminal dir() lists what other cmmands can be done in accordance with dir
#i.e dir(float), dir(int), dir(str)
#can use help(str.upper) to find specific uses of it

w="hello".upper() #prints out a string in uppercase for example
print(w)

test_add=("deez").__add__("nuts")
print(test_add)

#dir(__builtins__) states ALL already built in functions

#CODE THAT CREATES RANDOM LIST WITHIN SET RANGE

# Python code to generate random numbers and append them to a list 
# i.e can do thigs like x=list()
import random 

# Function to generate and append them 
# start = starting range, 
# end = ending range 
# num = number of 
# elements needs to be appended 
def Randy(start, end, num): 
	res = [] 

	for j in range(num): 
		res.append(random.randint(start, end)) 

	return res 

# Driver Code 
num = 15
start = 80
end = 100
print(Randy(start, end, num)) 

x=Randy(start, end, num)

sumofx=sum(x)
length=len(x) #finding the length/values of a list
mean=sumofx/length #calculating the mean of the list
mean=round(mean,2)
print(mean)  

#DICTIONARIES: another form of data type
student_grades={"Bobby":98,"Mikey":87,"Karen":69}
print(student_grades)
sumofstudents=sum(student_grades.values())
length=len(student_grades.keys())
meanofstudents=sumofstudents/length
meanofstudents=round(meanofstudents,2)
print(meanofstudents)

#TUPLES: Similar to lists but different in some cases
y=(1,2,3,4) #tuple use parenthesis rather than brackets

