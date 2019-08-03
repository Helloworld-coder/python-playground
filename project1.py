
"""
output=[]
def singlelist(l):
    for i in l:
        if type(i)==list:
            singlelist(i)
        else:
            output.append(i)
    return(output)

fruits=["apple","mango","orange","litchi"]
veggie=["carrot","beans","raddish","spinach"]
fruits.insert(1,veggie)
bag=fruits
result=singlelist(bag)
print(result)
"""
Input = ['Geeeks, Forgeeks', '65.7492, 62.5405', 
         'Geeks, 123', '555.7492, 152.5406']
temp=[]
for elem in Input:
    temp2 = elem.split(', ')
    temp.append((temp2))  
    print(temp)



    
