Time = input("Enter Time Like '00:00:00' : ")
Counter = 0
Hour = ""
Min = ""
Sec = ""
for i in Time:
    Counter += 1
    if Counter < 3:
        Hour = Hour + i
    if Counter > 3 and Counter < 6:
        Min = Min + i
    if Counter > 6:
        Sec = Sec + i
        
Total_Seconds = int(Sec) + int(Min)*60 + int(Hour)*60*60

print("Total Seconds is: " , Total_Seconds)