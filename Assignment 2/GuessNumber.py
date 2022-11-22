import random

Computer_Number = random.randint(10, 40)
Counter = 0

while True:
    Uesr_Number = int(input("Enter Your Guess:"))
    Counter +=1
    if Computer_Number == Uesr_Number:
        print("🎉🎉🎉🎉🎉")
        print("You Win")
        print("🎉🎉🎉🎉🎉")
        print("Number Of Your Guess: " , Counter)
        break
    elif Computer_Number > Uesr_Number:
        print("Go UP")
        print("⬆")

    elif Computer_Number < Uesr_Number:
        print("Go Down")
        print("⬇")
        