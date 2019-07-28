# covert the comma separated string into semicolon separated string
"""
def convert(fruit,a,b):
    result=fruit.replace(a,b)
    print(result)

fruit=("apple,orange,mango,chikku")
convert(fruit,",",":")


fruits=["apple","orange","mango","chikku","gvuva","papaya","grape","melon","amla","banana"]
fruits.reverse()
print(fruits)
#for fruit in range(1,10,2):
#    print(fruits[fruit])




fruits=["apple","orange","papaya","avacado"]
for r in range(0,3):
    print(fruits[r])


#going to assess the speed of the car
#using loops and boolean

def speedOfTheCar (speed):
    carspeed=True
    if speed > 80:
        carspeed=False
        return "slow down"
    else:
        return "Safe driving"

data=input("speed of the car: ")

#compare the speed of the car
def compare(car1,car2):
    if car1 < car2:
        return "car 1 is efficient"
    else:
        return " car 2 is efficiet"
car1=data
car2=input("enter the speed of the car2: ")

fruits=["apple","oak","guvavu"]
for fruit in range(fruits):
    print(fruits.int([0,1]))


i=0
while i<10:
    print(i)
    i+=5       # this is equal to i=i+1

# index()
    # retuns the position or index of the given argument.
laptopnames=["lenovo","hp","dell","apple"]
checkPosition=laptopnames.index("dell")
print(checkPosition)



#dot    -   means 0 run
#no     -   means 1 run
#wide   -   means 1 run
#four   -   means 4 run
#six    -   means 6 run
runtypes={"dot":0,"no":1,"wide":1,"four":4,"six":6}
def addRun(runtype,run,score):
        return score+int(runtypes[runtype])


x=input("enter the runtype: ")
y=input("enter the run: ")
z=input("enter the old score: ")
currenScore=addRun(x,int(y),int(z))
print(currenScore)

"""
"""
scoreBoard={
    "totalRuns":99,
    "totalWickets":0,
    "totalOver":17,
    "totalExtras":4
}
print(scoreBoard)

def runBoard(totalRuns,totalWickets,totalOver,totalExtras):
        totalRuns=totalRuns+4
        return {
            "totalRuns":totalRuns,
            "totalWickets":totalWickets,
            "totalOver":totalOver,
            "totalExtras":totalExtras      
            
        }
w=input("totalRuns: ")
x=input("totalWickets: ")
y=input("totalOver: ")
z=input("totalExtras: ")
ScoreBoard=runBoard(int(w),x,y,z)
print(ScoreBoard)

#from a string of fruits , check for the orange 
#then convert the string into list
# then replace orange with kiwi on position 1
# finally create a dictionary of fruits with respective kgs.


fruits=("apple orange melon mango papaya")
checkFruit=fruits.count("orange")
checkFruit=fruits.split()
checkFruit.remove("orange")
checkFruit.insert(0,"kiwi")
def fruitsbag(fruits,cost,fruits1,cost1):
        return {
            fruit:cost,
            fruits1:cost1
            
        }

fruit=input("enter the fruit1: ")
cost=input("enter the price: ")
fruits1=input("enter the second fruit: ")
cost1=input("enter the second price: ")
fruitbag=fruitsbag(fruit,cost,fruits1,cost1)
data=fruitbag.get("kiwi")
print(data)

"""
weapons=["guns","knives","swords","bombs","bullets"]
weapons.insert(1,"goli")
gadgets=weapons
print(gadgets)




















