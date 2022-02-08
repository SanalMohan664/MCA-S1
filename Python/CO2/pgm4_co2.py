import math
lim1 = int(input("Enter starting limit: "))
lim2 = int(input("Enter ending limit: "))
li=[]
for i in range(lim1,lim2):
    if i>99 and i<1000:
        if i%2==0 and (math.ceil(math.sqrt(i)) ==  math.floor(math.sqrt(i))):
            li.append(i)
print(li)
