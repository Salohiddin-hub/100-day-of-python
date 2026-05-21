import random
def checker(guesses):
    """It checks the guessed number is high or low or match the random number """
    r_number=random.randint(1,100)
    is_game_running=True
    while is_game_running:
        print(f"You have {guesses} attempts remaining to guess the number.")
        u_number=int(input("Make a guess: "))
        if u_number == r_number:
            print(f"You got it! Answer was {r_number}")
            is_game_running=False 
        else:
            guesses-=1 
            if u_number > r_number:
                print("Too high")
            else:
                print("Too low")
            if guesses == 0:
                print("You have run out of guesses. Refresh the page to run again")
                is_game_running=False
            else:
                print("Guess again")          
def game():
    """It makes the game easy or hard and run the game"""
    print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100.")
    u_choice=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if u_choice == "easy":
        checker(guesses=10)
    elif u_choice == "hard":
        checker(5)
game()