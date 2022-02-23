"""A more structured version of Wordle!"""

__author__ = "730309291"


def contains_char(search: str, single: str) -> bool:
    """When given two strings, will return True if single character found in given word."""
    assert len(single) == 1
    i: int = 0
    while i < len(search):
        if single == search[i]:
            return True
        else:
            i += 1
    return False 


def emojified(guess: str, secret: str) -> str:
    """When given a guess, it will return a white or yellow box."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8" 
    resulting_emoji = ""
    i: int = 0 
    while i < len(secret): 
        if contains_char(secret, guess[i]):
            if secret[i] == guess[i]:
                resulting_emoji += GREEN_BOX
            else:
                resulting_emoji += YELLOW_BOX
        else:
            resulting_emoji += WHITE_BOX
        i += 1
    return resulting_emoji 


def input_guess(expected_length: int) -> str:
    """Prompts user for guess of certain length."""
    guess: str = input(f"Enter a {(expected_length)} character word: ")
    while len(guess) != expected_length:
        guess = (input(f"That wasn't {expected_length} chars! Try again: "))
    
    return(guess)


def main() -> None:
    """The entrypoint of the program and main game loop."""
    number_of_turns: int = 0
    secret: str = "python"
    winner: bool = False
    while not winner and number_of_turns < 6:
        print(f"=== Turn {number_of_turns + 1}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            winner = True
        number_of_turns += 1
    if winner:
        print(f"You won in {number_of_turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()