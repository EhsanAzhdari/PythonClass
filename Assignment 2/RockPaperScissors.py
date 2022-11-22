import random

Computer_Score = 0
User_Score = 0  
while Computer_Score != 3 and User_Score != 3:
    x = random.randint(1, 3)

    if x == 1:
        Computer_Choice = "Rock"
    elif x == 2:
        Computer_Choice = "Paper"
    elif x == 3:
        Computer_Choice = "Scissors"
    print("You Can Select One Of Them --> Rock | Paper | Scissors ")    
    User_Choice = input("Enter Your Choice: ")
    
    print("💻" , Computer_Choice,"VS." ,"🧑", User_Choice)

    if Computer_Choice == "Rock" and User_Choice == "Paper":
        User_Score += 1
        
    elif Computer_Choice == "Rock" and User_Choice == "Scissors":
        Computer_Score += 1
    
    elif Computer_Choice == "Rock" and User_Choice == "Rock":
        print("Ops.. Both Choice Same as together!")
        
    elif Computer_Choice == "Scissors" and User_Choice == "Paper":
        Computer_Score += 1
        
    elif Computer_Choice == "Scissors" and User_Choice == "Scissors":
        print("Ops.. Both Choice Same as together!")
        
    elif Computer_Choice == "Scissors" and User_Choice == "Rock":
        User_Score += 1
    
    elif Computer_Choice == "Paper" and User_Choice == "Paper":
        print("Ops.. Both Choice Same as together!")
        
    elif Computer_Choice == "Paper" and User_Choice == "Scissors":
        User_Score += 1

    elif Computer_Choice == "Paper" and User_Choice == "Rock":
        Computer_Score += 1


if User_Score == 3:
    print("🎉🎉🎉🎉🎉")
    print("You Win")
    print("🎉🎉🎉🎉🎉")
else:
    print("👊👊Computer Win👊👊")