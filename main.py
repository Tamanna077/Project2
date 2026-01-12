# An Rule Based AI ChatBot

import datetime
import time

name = input("Enter your name")
present = datetime.datetime.now().hour

if 5 <= present <= 11:
    print("Good Morning! ",name)
elif 11 <= present <= 17:
    print("Good Afternoon! ",name)
elif 17 <= present <= 20:
    print("Good Evening! ",name)
else:
    print("Good Night! ",name)


print("Hello!!..Welcome to your ChatBot")
print("You can ask me a basic question. Type EXIT to close chat.")

# response dictionary for chatbot

Responses = {
    "hello": "hi..how may I help you? ",
    "who are you": "I am a smart AI ChatBot",
    "how are you": "I am fine! Thank You.",
    "motivate me": "Every bug of your project makes you a better developer",
    "happy": "Great to hear that :)",
    "sad": "I'm sorry :( ..How can i help you? "
}

# FUNCTION motivate

def resofbot(userInput):
    userInput = userInput.lower()
    for eachKey in Responses:
        if eachKey in userInput:
            return Responses[eachKey]
    return "I am not able to answer that!!.. I'll learn it soon!"

# user Input 

while True:

    userInput = input("Enter your question here: ")   
    reply = resofbot(userInput) 
    time.sleep(1) 
    print("Bot Response : ", reply)    

    if "exit" in userInput:
        break
