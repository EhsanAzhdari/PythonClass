Num1 = int(input("Enter Number 1 : "))
Num2 = int(input("Enter Number 2 : "))
BMM = 0
if Num1 > Num2:
    temp = Num2
else:  
    temp = Num1
for i in range(1 , temp + 1):  
    if (( Num1 % i == 0 ) and ( Num2 % i == 0 )):  
        BMM = i
print("BMM =", BMM)