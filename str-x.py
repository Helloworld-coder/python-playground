# string methods will be explored here
"""
# capitalize() method    
        #convers the first letter of string into caps
names=("jana ram laxman arun")
convertednames=names.split()
convertednames=names.capitalize()
print(convertednames)

# casefold() method

names=("jana ram laxman arun")
convertednames=names.split()
convertednames=names.casefold()
print(convertednames)

# lower() method
# upper() method

names=("jana ram laxman arun")
convertednames=names.split()
convertednames=names.upper()
print(convertednames)

# expandtabs() method


# count() method

name="what is my name, is it Jana"
findName=name.count("Jana")
print(findName)
# find() method
    #The find() method finds the first occurrence of the specified value.
    #The find() method returns -1 if the value is not found.
    #The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found
name="what is my name, is it Jana"
findName=name.find("jana")
print(findName)
# format() method
    #You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
    #The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
Demographics= "i am {2}, working as a {1} in {0}"
name="jana"
designation="data scientist"
company="irontron"
FinalData=Demographics.format(company,designation,name)
print(FinalData)

# replace () method
  # going to replace a set of brands
brands=("gm lg sony apple sanofi")
brandnames=brands.replace("gm","amul")
brandnames=brandnames.split(" ")
print("The available brands are" + str(brandnames))

# split () method
# strip () method
    #The strip() method removes any whitespace from the beginning or the end:
    #also removes the string given as argument

"""
import Dictionary_methods
a=Dictionary_methods.cars
print(a)