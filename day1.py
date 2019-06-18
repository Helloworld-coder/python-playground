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
        a=sum(data)
        print(a)                         

data=[100,200,400,500,300,600]
countArray(data)
