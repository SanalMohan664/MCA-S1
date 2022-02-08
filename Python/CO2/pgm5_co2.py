n=int(input("enter the step number: "))
for x in range(1, n+1):
    for y in range(1, x+1):
        print(x*y, " ", end="")
    print()
