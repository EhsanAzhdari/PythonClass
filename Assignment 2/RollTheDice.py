import random

Start = int(input("For Roll The Dice Enter '1' And for EXIT Enter '2':"))
while True:
    if Start == 1:
        Dice = random.randint(1, 6)
        if Dice < 6:
            print("Your Number: ", Dice)
            break
        else:
            print("Wow.. Your Number is 6 and You Can Roll The Dice Again🎉")
            Start = int(input("For Roll The Dice Enter '1':"))
    else:
        break
print("Finish..")
