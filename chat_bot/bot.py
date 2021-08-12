import random 

def respond(message):
    if message in responses:
        bot_message = random.choice(responses[message])
    else:
        bot_message = random.choice(responses["default"])

    return bot_message

def related(x_text):
    if "name" in x_text:
        y_text = "What's your name?"
    elif "weather" in x_text:
        y_text = "What's today's weather?"
    elif "robot" in x_text:
        y_text = "Are you a robot?"
    elif "how are" in x_text:
        y_text = "How are you?"
    else:
        y_text = ""

    return y_text

def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))

def start_bot():
    while 1: 
        my_input = input() 
        my_input = my_input.lower() 
        related_text = related(my_input) 
        send_message(related_text)
        
        if my_input == "exit" or my_input == "stop": 
            break

if __name__ == "__main__":
    print("BOT: What do you want me to call you?")
    user_name = input()

    bot_template = "BOT : {0}"
    user_template = user_name + " : {0}"

    name = "Bot"
    weather = "rainy"
    mood = "Happy"

    responses = {
        "What's your name?":[
            "They call me {0}".format(name),
            "I usually go by {0}".format(name),
            "My name is the {0}".format(name)],
        "What's today's weather?":[
            f"The weather is {weather}.",
            f"It's {weather} today.",
            f"Let me check, it looks {weather} today."
        ],
        "Are you a robot?":[
            "What do you think?",
            "Maybe yes, Maybe no!",
            "Yes, I am a robot with human feelings."
        ],
        "How are you?":[
            f"I am feeling {mood}",
            f"{mood}! How about you?",
            f"I am {mood}! How about yourself?"
        ],
        "":[
            "Hey!, are you there?",
            "What do you mean by saying nothing?",
            "Sometimes saying nothing tells a lot :)"
        ],
        "default":[
            "This is a default message"
        ]
    }

    start_bot()