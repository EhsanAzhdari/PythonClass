import gtts

def read_from_file():
    global words_bank
    
    f = open("Translate.txt", "r")
    temp = f.read().split("\n")
    
    words_bank = []
    for i in range(0, len(temp), 2):
        my_dict = {"en": temp[i], "fa": temp[i+1]}
        words_bank.append(my_dict)
    f.close()
    
def write_to_file():
    En_word = input("Enter English word: ")
    Fa_word = input("Enter Persian word: ")
    words_bank.append({"en": En_word, "fa": Fa_word})
    
    f = open("Translate.txt", "a")
    f.write("\n" + En_word + "\n"+ Fa_word)
    f.close()
    print("New Word Added..")
    
def translate_english_to_persian():
    user_text = input("Enter Your English Text: ")
    user_words = user_text.split(" ")
    output = ""
    
    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
                output = output + word["fa"] + " "
                break
        else:
            output = output + user_word + " "

    print(output)
    
def translate_persian_to_english():
    user_text = input("Enter Your Persian Text(separated sentences by '.'): ")
    user_Sentence = user_text.split(".")
    list_user_words = []
    for sentence in user_Sentence:
        temp = sentence.split(" ")
        list_user_words.append(temp)
    
    output = ""
    
    for list in list_user_words:
        for user_word in list:
            for word in words_bank:
                if user_word == word["fa"]:
                    output = output + word["en"] + " "
                    break
            else:
                output = output + user_word + " "

    print(output)

    voice = gtts.gTTS(output, lang="en", slow=False)
    voice.save("voice.mp3")
    
def show_menu():
    print("welcome to my translate")
    print("1- Translate English to Persian")
    print("2- Translate Persian to English")
    print("3- Add a New word to Database")
    print("4- Exit")
    
read_from_file()

while True:
    show_menu()
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        translate_english_to_persian()
    elif choice == 2:
        translate_persian_to_english()
    elif choice == 3:
        write_to_file()
    elif choice == 4:
        exit(0)
    

