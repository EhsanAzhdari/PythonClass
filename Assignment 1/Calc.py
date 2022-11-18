import math

print("************Calculator************")
print(" 1 --> + ")
print(" 2 --> - ")
print(" 3 --> * ")
print(" 4 --> / ")
print(" 5 --> sqrt")
print(" 6 --> Log")
print(" 7 --> Sin")
print(" 8 --> Cos")
print(" 9 --> Tan")
print("10 --> Cot")
print("11 --> Fact")


op = int(input("Please Enter Your Operation : "))
 

if op == 1 or op == 2 or op == 3 or op == 4:
    X = float(input("Number 1: "))
    Y = float(input("Number 2: "))

    if op == 1:
        result = X + Y

    elif op == 2:
        result = X - Y

    elif op == 3:
        result = X * Y

    elif op == 4:
        if Y == 0:
            result = "divide by zero!"
        else:
            result = X / Y


elif op == 5 or op == 6 or op == 7 or op == 8 or op == 9 or op == 10 or op == 11:
    A = float(input("Number: "))

    if op == 5:
        result = math.sqrt(A)
        
    elif op == 6:
        result = math.log(A)
        
    elif op == 7:
        result = math.sin(math.radians(A))

    elif op == 8:
        result = math.cos(math.radians(A))

    elif op == 9:
        result = math.tan(math.radians(A))

    elif op == 10:
        result = math.tan(math.radians(A))

    elif op == 11:
        result = math.factorial(int(A))


print(result)