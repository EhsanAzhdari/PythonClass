Snake_len = int(input("Enter Lenght Of Snake :"))

for i in range(1, Snake_len+1):
    if i % 2 == 0:
        print("#", end="")
    else:
        print("*", end="")