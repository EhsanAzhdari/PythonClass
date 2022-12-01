import random

Array_len = int(input("Enter Number: "))
Array_Num = []
Counter = 0
while Counter < Array_len:
    Random_Number = random.randint(0, 100)
    if Random_Number not in Array_Num:
        Array_Num.append(Random_Number)
        Counter +=1
        
print(Array_Num)