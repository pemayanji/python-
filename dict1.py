# Dictionary is a collection of items that allows us to store data in key value.

Marks={
    "Math":"97",
    "English":90,
    "Nepali":"76"
}

Capital={
    "Nepal":"Kathmandu",
    "India":"New Delhi",
    "China":"Beijing"
}

Capital.update(Marks)    # Combines two dictionary
print(Capital)

copied=Capital.copy()    #Copies
print("This is the copied dictionary",copied)
print("This is the original dictionary",Capital)

copied.clear()    #Clears
print(copied)

