Num = int(input("Enter Number : "))

fact = 1
Counter = 2
while True:
    fact = fact * Counter
    Counter += 1
    if fact == Num :
        print("YES")
        break
    if fact > Num :
        print("NO")
        break