#cls to clear (>) cntrl + L for (>>>)
#all the __function__ found in dir are hardly every used so ignore em basically
#in the help area where you see (self, object, /) that means it takes ONE argument in the function. self is usually the list/func itself
#in list.index it can look for values from any point to the beginning

wahoo=list(range(1,50,2))
wahoo.append(2.3)
#print(wahoo)
#wahoo.remove(2.3)
x=wahoo.index(13)
#print(x)
print(wahoo[0]) #gets the first index value!!!
print(wahoo[0:10])
print(wahoo[3:]) #gets the third index value and the rest from there!
print(wahoo[:10]) #starts from first index to the tenth
print(wahoo[-1]) #prints out the last index. good way to find index rather than counting. can also do SLICING still [the colon method]

#Scripts have values too!!!
x="deeznuts"
#print(x[0:4])
y=["deeznuts",1,2,3]
print(y[0][0:4])

#Dictionaries use KEYS instead of numerical values
student_grades={"Bobby":98,"Mikey":87,"Karen":69}
print(student_grades["Bobby"])