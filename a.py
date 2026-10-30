import nltk
from nltk.chat.until import Chat, reflection

reflections = {
    "i am"     : "you are",
    "i was"    : "you were",
    "i"        : "you",
    "i'm"      : "you are",
    "i'd"      : "i would",
    "i've"     : "you have",
    "i'll"     : "you will",
    "my"       : "your",
    "you are"  : "I am",
    "you were" : "I was",
    "you've"   : "I have",
    "you'll"   : "I will",
    "your"     : "my"
}

pairs = [
    [
        r" my name is (.*)",
        ["Hello %1, How are you today ?"]
    ]
    [
        r"hi|hey|hello"
        ["Helo", "Hey there"]
    ]
    [
        r"what do you do(.*)"
        ["I am a chatbot, I help people."]
    ]
    [
        r"Favourite car"
        ["BMW"]
    ]
]

def chat():
    print("Hi! I am a chatbot creatted by codingal Edu. Pvt. Lim. for your sevice")
    chat = Chat(pairs, reflection)
    chat.converse()

if__name__ =="__main__":
      chat()    