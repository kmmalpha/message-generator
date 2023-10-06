import random

def generate_romantic_message(name):
    messages = [
        "Thank you for all your support.",
        "I appreciate you and our friendship. <3",
        "I can't imagine my life without my bestie.",
        "You help make me a better person.",
        "I am so lucky to have you in my life.",
        "Thank you for being there for me.",
        "I hope Java does not kill you.",
        "You are a friend, indeed.",
        "I was not sure what to add at this point but just wanted to make the list a little bigger for the backend :P"
    ]

    message = random.choice(messages)
    message = message.replace("name", name)

    return message


if __name__ == "__main__":
    viable_names = ["Hlulani", "Baloyi", "Wifey", "Bestie", "Lani", "Hlulani Baloyi"]
    name = input("What is your name? ")
    
    if name in viable_names:
        message = generate_romantic_message(name)
        print(message)
    else:
        print("Bye! This was not meant for you!")

input()