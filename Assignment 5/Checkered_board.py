n = int(input("Enter Row OF Checkered board : "))
m = int(input("Enter Column OF Checkered board : "))

for i in range(1, n+1):
    for j in range(1, m+1):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
            print("#", end="")
        else:
            print("*", end="")
    print()