def weather_condition(temperature):
    if temperature >7:
        return "Warm"
    else:
        return "Cold"

#user_input=input("Enter temperature:") #input ONLY takes a string argument
#=(float(user_input)) #converts the user_input into a float instead of a string

#print(weather_condition(x))

user_input= input("Enter your first name: ")
user_input_2=input("Enter your last name: ")
user_input_3=input("Enter your weight: ")
message = "Hello %s" % user_input #older versionbnm,
message = f"Hello {user_input.title()} {user_input_2.title()}, why are you so fat? \n you weigh {user_input_3} lbs wtf??" #use this method 
print(message)