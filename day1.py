# This is my understanding about python


#print("hello world")
"""
def findMyCar(cars,find):
    for car in cars:
        if car == find:
            print ("hey i found you car "+ find)
                
cars=["ford","honda","hyundai","bmw","maruthi","maserati","hummer"]
#findMyCar(cars,"hummer")


def findMyCar(cars,find):
    carNotFound=True
    for car in cars:
        if car == find:
            carNotFound=False
            print ("hey i found you car "+ find)
    if carNotFound:
        print("car not found") 

cars=["ford","honda","hyundai","bmw","maruthi","maserati","hummer"] 
findMyCar(cars,"bmw")  

import cars
data=["ford","honda","hyundai","bmw","maruthi","maserati","hummer"]
cars.findMyCar(data,"hummer")

a=cars.add()
print(a)

h=cars.IsEngineHot(30)
if h:
        print("engine is hot")
else:
        print("engine ok carry on")


x=input("enginespeed:")
k=cars.enginespeed(int(x))
if k:
        print("low your speed")
else:
        print("safe driving")


import cars
t=input("enter temp:")
c=cars.roomtemp(int(t))
if c:
        print("switch on AC")
else:
        print("Temp is normal")

b=input("first number:")
c=input("second number:")
a=cars.addition(int(b),int(c))
print(a)


d=input("num1:")
e=input("num2:")
f=cars.sub(int(d),int(e))
print(int(f)


def findmycar(find):
        carfound=True
        for car in cars:
                if car==find:
                        carfound=False
                        print("the car is found")
        if carfound:
                print("car not found")
cars=["bmw","maruthi","ferrari","ford"]


a=cars.addition(5,10)
print(a)


import cars
a=input("num1:")
b=input("num2:")
c=cars.div(int(a),int(b))
print(c)


a="testing LOWERCASE"
b=a.casefold()
print(b)

a="testing uppercase"
b=a.capitalize()
print(b)

a="testing Center"
b=a.center(20)
print(b)

a="Testings Count"
b=a.count("s")
print(b)

c="Testing oF Find".find("oF")
print(c)

a="Testing the {} Format using {} price"
b=a.format("command",50)
print(b)

a=("Testing","join")
b="F".join(a)
print(b)

a="Testing the lsrtip"
b=a.lstrip("Testing the")
print(b)

c="Testing a new string method"
b=c.replace("s","S",1)
print(b)

a="Testing the split"
b=a.split()
print(b)

a="Testing the split with separating the given argument"
b=a.split("t")
print(b)

a="Testing the split with separating the given argument and times"
b=a.split("t",4)
print(b)



namedata=" jana ram lax arun anbu sankar "
namedatalen=len(namedata)
names=namedata.strip()
names=names.split(" ")
namelength=len(names)
#modname=names.upper()
#createlist=modname.split()
print("The length of the given string is: {} and the list length is: {}".format(namedatalen,namelength))

"""
def addnumber(a=10,b=40):
        c=a+b
        return c       

a=input("num1:")
b=input("num2:")
c=addnumber(int(a),int(b))
print(c)

