def generate_rug(n):
	rug = []
	
	for i in range(n):
		rug.append([0] * n)
		for j in range(n):
			rug[i][j] = max(abs(n//2 - i),abs(n//2 - j))
	
	return rug


while True:
    n = int(input("Enter Odd Number to Draw Rug : "))
    if n%2 != 0:
        Rug = generate_rug(n)
        for row in Rug:
            for num in row:
                print(num , end = " ")
            print()
    else:
        print("***************")
        print("Wrong Number!!!")
        print("***************")