```
It creates an array of romantic messages.
It generates a random index between 0 and the length of the array.
It selects the message at the random index.
It replaces the word "name" in the message with the name that was passed as input.
It returns the message
```
function generateRomanticMessage(name) {
    const messages = [
        "I love you more than words can say.",
        "You are the light of my life.",
        "I can't imagine my life without you.",
        "You make me a better person.",
        "I am so lucky to have you in my life.",
        "'I don't wanna lose you now, or ever'",
        "'You're my sun and moon. Girl you're everything.'",
        "'A lot of pretty faces could waste time, but you're my dream girl'"
    ];

    const randomIndex = Math.floor(Math.random() * messages.length);
    let message = messages[randomIndex];
    message = message.replace("name", name);

    return message;
}

const viableNames = ["Buhlebendalo", "Buhle", "Serenity", "Alpha Serenity", "Ndalo"];

```
It gets the value of the text input field with the id nameInput.
It checks if the name is included in an array of viable names called viableNames.
If the name is included in the array of viable names, the function calls the generateRomanticMessage() function to generate a romantic message.
If the name is not included in the array of viable names, the function generates a message that says "Bye! This was not meant for you!".
The function then sets the text content of the element with the id messageOutput to the generated message
```
function generateMessage() {
    const name = document.getElementById("nameInput").value;
    let message = "";

    if (viableNames.includes(name)) {
        message = generateRomanticMessage(name);
    } else {
        message = "Bye! This was not meant for you!";
    }

    document.getElementById("messageOutput").textContent = message;
}