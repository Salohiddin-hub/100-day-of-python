import random    
logo="""
     ------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    '-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
        |  \/ K|                            _/ |                
        '------'                           |__/ """
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def comparison(user_card, computer_card):
    if 11 in user_card:
        user_card.remove(11)
        user_card.append(1)
    elif 11 in computer_card:
        computer_card.remove(11)
        computer_card.append(1)
    if sum(user_card) == sum(computer_card):
        return "Draw!"
    elif sum(computer_card) == 21 and len(computer_card) == 2:
        return "Computer won with BlackJack!"
    elif sum(user_card) == 21 and len(user_card) ==2:
        return " You won with BlackJack!" 
    elif sum(user_card) > 21:
        return "You burst! You lose!"
    elif sum(computer_card)>21:
        return "I burst! You won!"
    elif sum(user_card)>sum(computer_card):
        return "You won!"
    elif sum(user_card)<sum(computer_card):
        return "You lose!"
is_game_running=True
print(logo)
while is_game_running:
    user_card=[]
    computer_card=[]
    for i in range(0,2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    start=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start =="y":
        print(f"You cards: {user_card}. Current score:{sum(user_card)}\n",
              f"Computer's first card: {computer_card[0]}")
        user=input("Type 'y' to get another card, type 'n' to pass: ")
        while user == "y":
            user_card.append(deal_card())
            print(f"You cards: {user_card} and Current score {sum(user_card)}\n ",
                f"Computer cards: {computer_card}")
            if sum(user_card)>21 or sum(computer_card)>21:
                print(comparison(user_card, computer_card))
                break
            else:
                user=input("Type 'y' to get another card, type 'n' to pass: ")
                while sum(computer_card) < 17:
                    computer_card.append(deal_card())
                if user == "n":
                    print(f"You cards: {user_card} and current score {sum(user_card)}\n",
                        f"Computer cards: {computer_card} and current score {sum(computer_card)}")
                    print(comparison(user_card, computer_card))           
    elif start == "n":
        print(comparison(user_card, computer_card))
        is_game_running=False  
