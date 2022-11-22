N = int(input("Please Enter the Number to Calculate the Fibonacci series:"))

print("1" , end="")
Fibo = 1
temp1 = 0
for i in range(1,N):
    temp2 = Fibo
    Fibo = Fibo + temp1
    temp1 = temp2
    print(",",Fibo,end="")