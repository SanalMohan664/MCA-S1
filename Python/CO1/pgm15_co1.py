clr_list1=["violet","yellow","blue","white","black"]
clr_list2=["violet","black","orange","green","yellow"]
print(clr_list1)
print(clr_list2)
print("all colors from color-list1 not contained in color-list2")
print([x for x in clr_list1 if x not in clr_list2])
