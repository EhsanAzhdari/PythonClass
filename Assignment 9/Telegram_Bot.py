import random
import telebot
from khayyam import JalaliDatetime
import gtts
import qrcode

bot = telebot.TeleBot("5916062640:AAGu7HI3xphYwzJgUNxvAiExGRFP__8P7BY", parse_mode = None)

@bot.message_handler(commands = ["start"])
def start(message):
    bot.reply_to(message, f"Hey! {message.from_user.username} \n Welcome To The EHSAN BOT")


@bot.message_handler(commands = ["help"])
def help(message):
    Help_string = """
    /start  - Start Bot
    /game   - Start GuessNumber GAME
    /age    - Get Birthdate And Calculate Your Age
    /voice  - Convert English Text To Voice
    /max    - Get Array And Calculate MAX Number
    /argmax - Get Array And Calculate MAX Index Number
    /qrcode - QR Code Generator
    /help   - Help Bot
    """
    bot.reply_to(message, Help_string)

Keyboard = telebot.types.ReplyKeyboardMarkup(row_width = 1, resize_keyboard=True)
Key = telebot.types.KeyboardButton("New Game")
Keyboard.add(Key)

@bot.message_handler(commands = ["game"])
def send_Game(message):
    global Computer_Number
    Computer_Number = random.randint(1, 50)
    Message = bot.send_message(message.chat.id, "Enter Your Guess (between 1 - 50):")
    bot.register_next_step_handler(Message, gameMessage)

def gameMessage(message):
    global Computer_Number
    if message.text == "New Game":
        Computer_Number = random.randint(1, 50)
        Message = bot.send_message(message.chat.id, "New Game Started..  Enter Your Guess:")
        bot.register_next_step_handler(Message, gameMessage)
    elif int(message.text) < Computer_Number:
        Message = bot.send_message(message.chat.id, "⬆ Go UP ⬆", reply_markup = Keyboard)
        bot.register_next_step_handler(Message, gameMessage)
    elif int(message.text) > Computer_Number:
        Message = bot.send_message(message.chat.id, "⬇ Go Down ⬇", reply_markup = Keyboard)
        bot.register_next_step_handler(Message, gameMessage)
    elif int(message.text) == Computer_Number:
        bot.send_message(message.chat.id, "🎉You Win🎉", reply_markup = Keyboard)
            

@bot.message_handler(commands=['age'])
def send_Age(message):
    Message = bot.reply_to(message, " Enter Shamsi BirthDate to Calculate Age (Correct Style --> 1300/01/01): ")	
    bot.register_next_step_handler(Message, Age_Message)
	
def Age_Message(message):
    list = message.text. split("/")
    AllDays = JalaliDatetime.now() - JalaliDatetime(list[0],list[1],list[2])
    AgeYear = AllDays.days // 365
    AllDays = AllDays.days % 365
    AgeMonth= AllDays // 30
    AgeDays = AllDays % 30 - 7
    bot.send_message(message.chat.id, f"Years:{AgeYear} Months:{AgeMonth} Days:{AgeDays}" )


@bot.message_handler(commands = ["voice"])
def send_Voice(message):
    Message = bot.send_message(message.chat.id, "Enter Your English Text :")
    bot.register_next_step_handler(Message, voice_Message)
    
def voice_Message(message):
    voice = gtts.gTTS(message.text, lang="en", slow=False)
    voice.save("voice.mp3")
    play_sound = open("voice.mp3", "rb")
    bot.send_voice(message.chat.id, play_sound)



@bot.message_handler(commands = ["max"])
def send_MAX(message):
    Message = bot.send_message(message.chat.id, "Enter Array (Correct Style --> 1,2,3,4,5)")
    bot.register_next_step_handler(Message, MAX_Message)
    
def MAX_Message(message):
    Numbers = list(map(int, message.text.split(",")))
    MAX = max(Numbers)
    bot.reply_to(message, f"MAX is : {MAX}")


@bot.message_handler(commands = ["argmax"])
def send_argmax(message):
    Message = bot.send_message(message.chat.id, "Enter Array (Correct Style --> 1,2,3,4,5)")
    bot.register_next_step_handler(Message, argMAX_Message)
    
def argMAX_Message(message):
    Numbers = list(map(int, message.text.split(",")))
    index = Numbers.index(max(Numbers))
    bot.reply_to(message, f"MAX Index is : {index}")


@bot.message_handler(commands = ["qrcode"])
def send_QRcode(message):
    Message = bot.send_message(message.chat.id, "Enter Your Text :")
    bot.register_next_step_handler(Message, QR_Message)
    
def QR_Message(message):
        QR = qrcode.make(message.text)
        QR.save("QRcode.png")
        QRcodeFile = open("QRcode.png", "rb")
        bot.send_photo(message.chat.id, QRcodeFile)

bot.infinity_polling()