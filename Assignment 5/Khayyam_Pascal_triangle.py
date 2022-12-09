n = int(input("Enter Row OF Khayyam Pascal Triangle : "))

Pascal = []
for i in range(1, n + 1):  
    NUM = 1
    Pascal.append([])
    for j in range(1, i + 1):
        Pascal[i - 1].append(NUM) 
        NUM = int(NUM * (i - j) / j)


for i in range(len(Pascal)):
    for j in range(len(Pascal[i])):
        print(Pascal[i][j], "\t", end="")
    print()