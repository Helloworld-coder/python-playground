#append()
    # adds only 1 string to the list
    
mobiles=["apple","samsung","sony","nokia","lg"]
mobiles.append("asus")
print(mobiles)

    # adds multiple strings when given inside []
mobiles=["apple","samsung","sony","nokia","lg"]
mobiles.append(["asus","lenovo"])
print(mobiles)

# extend
    # joins the new list to the end of the previous list
    # differs from append since it joins 2 list whereas append donot join two lists as one.
cars = list(("hummer","maserati","ferrari","ford"))
carsModels= ["gt","mustang","murcielago","accord"]
#cars.extend(carsModels)
print(cars)
 

#insert()
    # uses index - inserts the item at a specified index
cars=["bmw","benz","honda","hyundai"]
cars.insert(1,"hummer")
totalCars=cars
print(totalCars)

#remove()
    # removes an item from the list
weapons=["guns","knives","swords","bombs","bullets"]
weapons.remove("knives")
gadgets=weapons
print(gadgets)

#pop()
    # uses index - removes the item from the specified index or the last item - if not specified
weapons=["guns","knives","swords","bombs","bullets"]
weapons.pop(1)
gadgets=weapons
print(gadgets)

#del
    # mainly deletes the entire list
    # uses index - deletes the item from the given index
    # del list method is used before the list name
weapons=["guns","knives","swords","bombs","bullets"]
del weapons[4]
gadgets=weapons 
print(gadgets)

# clear()
    # clears the entire list
    # no arguments should be given under ()
pharmabrands=["sanofi","pfizer","cipla","ranbaxy"]
pharmabrands.clear()
print(pharmabrands)

# copy()
    # makes a copy of the list to another list name or variable
laptopnames=["lenovo","hp","dell","apple"]
newnames=laptopnames.copy()
print(newnames)

# list()
    # makes a copy of the list to another list name or variable
laptopnames=["lenovo","hp","dell","apple"]
newnames=laptopnames.copy()
print(newnames)

# sort()
    # sorts the list items as per order
laptopnames=["lenovo","hp","dell","apple"]
laptopnames.sort()
reversedname=laptopnames
print(laptopnames)

# reverse()
    # reverse the entire list
laptopnames=["lenovo","hp","dell","apple"]
reversedname.reverse()
print(reversedname)

# count()
    # returns the number of repeats of the given argument, if not returns 0.
    # should assign to a variable and then returns or print the output.
laptopnames=["lenovo","hp","dell","apple"]
checkNames=laptopnames.count("apple")
print(checkNames)    

# index()
    # retuns the position or index of the given argument.
    # should assign to a variable and then returns or print the output.
laptopnames=["lenovo","hp","dell","apple"]
checkIndex=laptopnames.index("dell")
print(checkIndex)
