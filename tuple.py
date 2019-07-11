weeks_t=("sunday","sunday","tuesday","wednesday","thursday","friday","saturday")
x=weeks_t.count("sunday")
print(x)

weeks_l=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
weeks_l[3]="goodday"
#print(weeks_l)

lotteryList=[25,35,45,55,65]
#print(min(lotteryList))

def min_max(minmax):
    mi=min(minmax)
    mx=max(minmax)
    ln=len(minmax)
    return(mi,mx,ln)
minmax=[2,4,6,8,10]
a,b,c=min_max(minmax)
print("The minimum value is: {}".format(a))
print("The maximum value is: {}".format(b))
print("The length of the list is: {}".format(c))




