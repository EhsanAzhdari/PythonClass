n = int(input("Enter Row OF Multiplication table : "))
m = int(input("Enter Column OF Multiplication table : "))

for i in range(1, n+1):
    for j in range(1, m+1):
        print(i*j, "\t", end=" ")
    print()