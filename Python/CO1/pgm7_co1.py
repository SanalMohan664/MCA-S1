l1=[2,14,6,17,8]
l2=[17,43,5,75,9]
print(l1)
print(l2)

#a
if len(l1)==len(l2):
    print("list are of same length")
else:
    print("List are not of same length")


#b
if sum(l1)==sum(l2):
    print("List are of same sum")
else:
    print("List are not of same sum")

#c
a=[x for x in l1 if x in l2]
if len(a)<1:
    print("No value occure in both")
else:
    print("common values:",a)
