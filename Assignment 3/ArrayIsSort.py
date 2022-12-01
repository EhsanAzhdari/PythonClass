Array = []
print("Create Array")
while True:
    x = input("Enter Number OR Type 'EXIT' :")
    if x == "EXIT":
        break
    Array.append(int(x))

flag = 0
for i in range(len(Array)):
    for j in range(i+1, len(Array)):
        if Array[i] > Array[j]:
            print("Array Not Sorted")
            flag = 1
            break
    if flag == 1:
        break        
if flag == 0:
    print("Array Sorted")    