Capital={
    "Nepal":"Kathmandu",
    "India":"New Delhi",
    "China":"Beijing"
}
print(Capital)
print(len(Capital))
print(type(Capital))

print(Capital.keys())   # Gives list of keys in the dictionary
print(Capital.values())   # Gives list  of values in the dictionary

print(Capital["Nepal"])   #Gives the value of the key

Capital["Japan"]="Tokyo"    # Adds the value in the dictionary
print(Capital)

Capital["Bhutan"]="Thimpu"
print(Capital)

pop_element = Capital.pop("India")
print(pop_element)
print(Capital)