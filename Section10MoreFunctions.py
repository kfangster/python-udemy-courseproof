#to add more into functions you can use , to add more
def add(a, b):
    return a + b
#this can take default parameters
#arguments can take nonkeyword or keyword arguments (2 or b=2 both works)

#to add multiple/as many arguments as you want then use a * on the side to add a lot of arguments
def mean(*amount):
    return sum(amount)/ len(amount)
#to call arguments here they can only be nonkeyword arguments



#this is used for dictionaries and other determining methods such as this
def mean2(**kwamount): #keys and values (keywords)
    return kwamount
#allows for keyword arguemnts


