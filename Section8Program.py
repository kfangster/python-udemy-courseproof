def edit_string(stringname):
    capitalized=stringname.capitalize()
    punctuation= ("how", "what", "why","when","where","How","What","Why")
    if stringname.startswith(punctuation):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

this_list=[]

while True:
    data_text=input('Say something:')
    #for i in range(1):
        #this_list.append(data_text)
    if data_text == "\end":
        break
    else:
        this_list.append(edit_string(data_text))

print(" ".join(this_list))