output=[]
def NestedToFlatList(cars):
    for car in cars:
        if type(car)==list:
            NestedToFlatList(car)
        else:
            output.append(car)
    return(output)

