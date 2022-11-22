Total_Sec = int(input("Enter Seconds : "))

Hour = Total_Sec // 3600
Min = (Total_Sec % 3600) // 60
Sec = (Total_Sec % 3600) % 60

if Hour < 10:
    Hour = "0" + str(Hour)
if Min < 10:
    Min = "0" + str(Min)
if Sec < 10:
    Sec = "0" + str(Sec)
    
print(f"{Hour}:{Min}:{Sec}")