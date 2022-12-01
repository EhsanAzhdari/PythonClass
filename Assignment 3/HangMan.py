import random

words_bank = ["think", "beard", "blue", "train", "fish", "woman", "life", "freedom", "iran", "sky"]
user_mistakes = 0

good_chars = []
bad_chars = []
x = random.randint(0, len(words_bank)-1)
word = words_bank[x]
Count_word = len(word)
Count_Correct = 0

while user_mistakes < 6:
    for i in range(len(word)):
        if word[i] in good_chars:
            print(word[i], end=" ")
        else:
            print("-", end=" ")
    if Count_Correct == Count_word:
        print("\nYou Win")
        print("✨🎉🎊")
        break
    user_char = input("Please Write Your Guess:").lower()
    if len(user_char) == 1:
        if user_char in word:
            good_chars.append(user_char)
            Count_Correct +=1
            print("✅")
        else:
            bad_chars.append(user_char)
            user_mistakes += 1
            print("❌")
    else:
        print("Mese Adam Vared Kon :|")
if user_mistakes == 6:
    print("Game Over 👊💀")
    
    