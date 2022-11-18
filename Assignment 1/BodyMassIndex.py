A = float(input("Please Enter your Weight: "))
B = float(input("Please Enter your Height: "))

BMI = A / (B * B)
print("Your BMI IS:", BMI)

if BMI < 18.5:
    print("BMI Result : Underweight")

elif BMI >= 18.5 and BMI < 25:
    print("BMI Result : Normal Weight")

elif BMI >= 25 and BMI < 30:
    print("BMI Result : Overweight")

elif BMI >= 30 and BMI < 35:
    print("BMI Result : Obesity")

elif BMI >= 35 and BMI < 40:
    print("BMI Result : Extreme Obesity")
    
else:
    print("Error! BMI Out Of Range")