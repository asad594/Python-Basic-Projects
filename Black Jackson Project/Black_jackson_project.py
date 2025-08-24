import random
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def getdegree():
    cards= [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    total=sum(cards)
    if total==21 and len(cards)==2:
        return 0
    if 11 in cards and total>21:
        cards.remove(11)
        cards.append(1)
    return total

def compare(u_score, c_score):
    if u_score==c_score:
        return "Draw"
    elif u_score==0:
        return "With with a blackjack"
    elif c_score==0:
        return "You lose Opponent has a blackjack"
    elif u_score>21:
        return "You went over . You lose"
    elif c_score>21:
        return "Opponent went over .You win "
    elif u_score>c_score:
        return "You win"
    else:
        return "You lose"
def play_again():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score=-1
    user_score=-1
    is_game_over=False
    for _ in range(2):
        new_card=getdegree()
        user_cards.append(new_card)
        computer_cards.append(new_card)
    while not is_game_over:
        computer_score=calculate_score(computer_cards)
        user_score=calculate_score(user_cards)
        print(f"Your cards : {user_cards} , current score : {user_score}")
        print(f"Computer card: {computer_cards[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            print("Good Bye ")
            is_game_over=True
        else:
            choice=input("Type 'y' to get another card or type 'n' to pass : ").lower()
            if choice=="y":
                user_cards.append(getdegree())
            else:
                print("Good Bye: ")
                is_game_over=True

    while computer_score!=0 and computer_score>17:
        computer_cards.append(getdegree())
        computer_score=calculate_score(computer_cards)
    print(f"your final hand is {user_cards} and final score is {user_score}")
    print(f"Computer final hand is {computer_cards} and computer final score is {computer_score}")
    print(compare(user_score,computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_again()