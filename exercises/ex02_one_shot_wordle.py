"""One shot wordle!"""

__author__ = "730309291"

secret: str = "python"

letter_guess: str = input(f"What is your {len(secret)}-letter guess? ") 

i: int = 0
resulting_emoji = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Ensures that input is proper length 
while len(letter_guess) != len(secret):
    letter_guess = str(input(f"That was not {len(secret)} letters! Try again: "))
# Message for correct input 
if letter_guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon! ") 
# Emoji feedback using boolean statements allows for options, True or False, Yellow or White 
while i < len(secret):
    if letter_guess[i] == secret[i]:
        resulting_emoji += GREEN_BOX
    else:
        bool_variable: bool = False
        h: int = 0
        while bool_variable is False and h < len(secret):
            if letter_guess[i] == secret[h]:
                bool_variable = True 
            else:
                h += 1
        if bool_variable is True:
            resulting_emoji += YELLOW_BOX
        else:
            resulting_emoji += WHITE_BOX
    i += 1
print(resulting_emoji)
