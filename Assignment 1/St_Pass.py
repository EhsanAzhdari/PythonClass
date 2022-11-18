Fname = input("Please Enter First Name Of Student: ")
Lname = input("Please Enter Last  Name Of Student: ")

Num1 = float(input("Enter First  Score: "))
Num2 = float(input("Enter Second Score: "))
Num3 = float(input("Enter Third  Score: "))

AVG = (Num1 + Num2 + Num3) / 3
print("Student :",Fname,Lname,"Average :",AVG)
  
if AVG >= 17:
    print("Great")

elif AVG < 17 and AVG >= 12:
      print("Normal")

elif AVG < 12:
    print("Fail")