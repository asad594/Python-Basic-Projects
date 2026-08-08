"""Treasure Island CLI Interactive Adventure Game.

Features branching narrative choice paths, riddles, item actions, and multiple victory/game-over outcomes.
"""

ASCII_ART = r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''


def yellow_room_path() -> None:
    """Handle yellow door path and ancient riddle challenge."""
    print("You open the yellow door.")
    print("A golden hallway stretches before you. At the end, there's a glowing pedestal with an ancient scroll.")
    print("\nTo claim the scroll, answer the Riddle of the Ancients:")
    print("  'I have cities, but no houses.'")
    print("  'I have mountains, but no trees.'")
    print("  'I have water, but no fish.'")
    print("  Who am I?")

    ans = input("Type 'map' or 'not map': ").strip().lower()
    if ans == "map":
        print("\n🎉 Correct! You have proven your wisdom.")
        print("The treasure is yours! You win the game and become a legendary adventurer! 🏆")
    else:
        print("\n💀 Wrong answer!")
        print("The walls close in and a trapdoor opens beneath your feet...")
        print("You fall into a pit of darkness. Game Over.")


def red_room_path() -> None:
    """Handle red door path and footsteps riddle challenge."""
    print("You open the red door and see a dark room bathed in glowing red light.")
    print("A voice echoes: 'Answer my question to get the treasure, or face the flames!'")
    print("\nRiddle: 'The more you take, the more you leave behind. What am I?'")
    print("  A. footsteps")
    print("  B. time")
    print("  C. money")

    answer = input("Type your answer: ").strip().lower()
    if answer == "footsteps" or answer == "a":
        print("\nCorrect! You solved the riddle.")
        print("A secret door opens revealing the ancient gold! 🎉 You win!")
    else:
        print("\nWrong answer!")
        print("🔥 The room ignites with fire. Game Over.")


def blue_room_path() -> None:
    """Handle blue door narrative choices."""
    print("You open a blue gate leading into a subterranean cave system.")
    choice = input("Type 'left' or 'right' to select your cavern direction: ").strip().lower()

    if choice == "right":
        print("You stumble into a den of hungry wild beasts! 🐆 Eaten by animals. Game Over.")
    elif choice == "left":
        print("You choose the left path. It's pitch dark and you cannot see your hand!")
        action = input("Type 'light torch' or 'go blind': ").strip().lower()

        if action == "light torch":
            print("The torch brightens the cavern, revealing an underground pond.")
            cross = input("How do you cross? Type 'build' to assemble a raft, 'fly' to swing across: ").strip().lower()

            if cross == "build":
                print("You gather floating driftwood, craft a sturdy raft, and cross safely.")
                print("🏆 You reach the inner sanctum and find the hidden treasure! You win!")
            else:
                print("As you swing across, a giant cavern beast catches you in mid-air. Game Over.")
        else:
            print("You walk blindly in darkness, trip over a ledge, and fall into a pit. 💀 Game Over.")
    else:
        print("Invalid directional choice. You wander lost forever. Game Over.")


def play_game() -> None:
    """Execute main interactive narrative sequence."""
    print(ASCII_ART)
    print("Welcome to Treasure Island!")
    print("Your mission is to find the treasure.")

    place = input("\nYou are at a cross road. Where do you want to go? Type 'left' or 'right': ").strip().lower()

    if place == "left":
        print("You have come to a wide lake. There is an island in the middle of the lake.")
        action = input("Type 'wait' to wait for a boat, or 'swim' to swim across: ").strip().lower()

        if action == "wait":
            print("A gentle ferryman arrives and brings you to the island unharmed.")
            color = input("You arrive at a house with 3 doors: 'red', 'yellow', or 'blue'. Which do you choose?: ").strip().lower()

            if color == "yellow":
                yellow_room_path()
            elif color == "red":
                red_room_path()
            elif color == "blue":
                blue_room_path()
            else:
                print("You chose a door that doesn't exist. Game Over.")
        else:
            print("You get attacked by angry water beasts while swimming! 🐊 Game Over.")
    else:
        print("You step into a concealed pit trap! 💀 Game Over.")


if __name__ == "__main__":
    play_game()
