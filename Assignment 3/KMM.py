Num1 = int(input("Enter Number 1 : "))
Num2 = int(input("Enter Number 2 : "))

for i in range (max(Num1,Num2), (Num1*Num2)+1):
     if(i%Num1==0 and i%Num2==0):
         KMM = i
         
print("KMM =", KMM)