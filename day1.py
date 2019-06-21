#print("hello world")

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
print(complex(f))


