import random

def generate_romantic_message(name):
    messages = [
        "I love you more than words can say.",
        "You are the light of my life.",
        "I can't imagine my life without you.",
        "You make me a better person.",
        "I am so lucky to have you in my life."
    ]

    message = random.choice(messages)
    message = message.replace("name", name)

    return message


if __name__ == "__main__":
    viable_names = ["Buhlebendalo", "Buhle", "Serenity", "Alpha Serenity", "Ndalo"]
    name = input("What is your name? ")
    
    if name in viable_names:
        message = generate_romantic_message(name)
        print(message)
    else:
        print("Bye! This was not meant for you!")
