Score = 0
SUM_Score = 0
Counter = 0
while Score != "EXIT":
    Score = input("Enter Your Score OR Type EXIT:")
    if Score.isdigit():
        SUM_Score += int(Score)
        Counter +=1
AVG = SUM_Score / Counter
print("Your Average is: ", AVG)