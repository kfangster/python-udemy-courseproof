#def mean(mylist):
    #the_mean=sum(mylist)/len(mylist)
    #print(the_mean)
    #return the_mean

#print(mean([1,4,5]))

#print(type(mean),type(sum))

#TRY TO USE RETURN RETURN makes sure the variable is returned into something that's not a function
#You can still use print though

#Conditionals
def mean(value,keys,legs,thighs):
    if type(value) == dict:
        the_mean=sum(value.values())/len(value)
    else:
        the_mean=sum(value)/len(value)
    return the_mean

grades_overall=[1,4,6,7,8,9,7,4,3,2,3,4,5,6,7,8]
student_grades={"Karen":89,"Bobby":69,"Kevin":62,"Daneil":96,"Jameson":72.4}
lolofmean=mean(student_grades)
lolofmean=round(lolofmean, 2)
#print(mean(grades_overall))

#inside the IF ELSE statements can use AND OR statements inside as well
x="wow"; y=0
#if x==1 or y==1:
   # print("deez nutz")
#else:
   # print("woop")

if isinstance(x,int): #returns whether an object is an instance of a class or of an subclass
    print(x*x)
elif isinstance(x,str):
    print ("FAILURE")
else: #ELSE Statements do not takie in any other statments to add must use elif!!!!!
    print("ruh roh raggy")

