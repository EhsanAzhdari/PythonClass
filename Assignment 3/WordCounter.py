Sentence = input("Enter Your Sentence :\n")
Words = 1

for i in Sentence:
    if i == " ":
        Words +=1

print("Number Of Words :" , Words)