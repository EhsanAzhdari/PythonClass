A = int(input("Enter Number 1 : "))
B = int(input("Enter Number 2 : "))
C = int(input("Enter Number 3 : "))

if A + B > C and A + C > B and B + C > A:
    print("Input Number is True")
else:
    print("Input Number is False")