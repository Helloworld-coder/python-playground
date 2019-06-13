#print("hello world")

def findMyCar(cars,find):
    for car in cars:
        if car == find:
            print ("hey i found you car "+ find)
                
cars=["ford","honda","hyundai","bmw","maruthi","maserati","hummer"]
findMyCar(cars,"hummer")


def findMyCar(cars,find):
    for car in cars:
        if car == find:
            print ("hey i found you car "+ find)
        
        elif car != find:
            print("car not found") 

cars=["ford","honda","hyundai","bmw","maruthi","maserati","hummer"] 
findMyCar(cars,"jaguar")  

