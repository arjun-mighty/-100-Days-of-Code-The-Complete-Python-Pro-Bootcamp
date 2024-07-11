programming_dictionary={
    "Bug":"Its a bug dude",
    "Function":"Its a function buddy",
}
# here bug is a key , inside it the value is present i.e key value pair
#here each key can have only 1 value, if we have multiple values then we need to use lists.
#print(programming_dictionary["Function"])

#adding new items to the dictionary
programming_dictionary["Loop"]="Its a loop dude"


#creating empty dictionar
empty_dictionary={}

#wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#edit an existing dictioanry
programming_dictionary["Bug"]="It is not a bug dude"
#print(programming_dictionary)

#loop through dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
    

#nesting a dictionary

capitals = {
    "USA":"Washington",
    "India":"New Delhi",
    "Germany":"Berlin",
}
#nesting a list in a dictionary
travelling_log = {
    "India":["Kerala","Kottayam","Trichy"],
    "Germany":["Berlin","Hamburg"],
}
#nesting a dictionary in dictionary
travelling_log = {
    "India":{"Cities visited":["Kerala","Kottayam","Trichy"],"Total cities visited":12},
    "Germany":{"Cities visited":["Berlin","Hamburg"],"Total cities visited":3}
}
#nesting a dictionary in a list
travelling_log = {
    {"Country":"India",
     "Cities visited":["Kerala","Kottayam","Trichy"],
     "Total cities visited":12
    },
    
    {"Country":"Germany",
     "Cities visited":["Berlin","Hamburg"],
     "Total cities visited":3
    }
}