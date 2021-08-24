temps = [221, 234, 235, 236]

new_temps= []

for temp in temps:
    new_temps.append(temp/10)

print(new_temps)

#OR

new_temps2=[temp/10 for temp in temps]

print(new_temps2)

#-----------------------------------------------------

temps = [221, 234, 235, 267, -9999]

new_temps= [temp/10 for temp in temps if temp != -9999]

print(new_temps)

#-----------------------------------------------------

temps = [221, 234, 235, 267, -9999, 2340, 2400]

new_temps= [temp/10 if temp != -9999 else 0 for temp in temps]

print(new_temps)

def foo(a, b):
    print(a + b)
