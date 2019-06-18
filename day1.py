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

def countArray(data):
        for num in data:
                x=(num)
                y=(num+x)
                print(y)
       
data=[100,200,400,500,300,600]
countArray(data)

def name(names,data):
        namenotfound=True
        for name in names:
                if name == data:
                        namenotfound=False
                        print("my name is "+ data)
        if namenotfound:
                print("name not found")                  

names=["jana","john"]
name(names,"ram")
name(names,"jana")



