print(r'''
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
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
place=input("You are at a cross road where do you want to go ? Type left or right ")
if place !="left" and place!="right":
     print("invalid input")
else:
    if place=="left":
        print("You have come to a lake.There is an island in the middle of lake ")
        action=input("Type wait to wait for a boat or type swim to swim across ")
        if action!="wait" and action!="swim":
            print("Invalid input")
        else:
            if action=="wait":
                print("You arrived at the island unharmed ")
                color=input("There is a house with three colours.\nOne red,One yellow,One blue ")
                if color!="red" and color !="yellow" and color!="blue":
                    print("Invalid input")
                else:
                    if color=="yellow":
                        print("You open the yellow door")
                        print("A golden hallway stretches before you. At the end, there's a glowing pedestal with an ancient scroll.")
                        print("But before you can take the treasure ans the riddle ")
                        print("The riddle is ")
                        print("Riddle of the Ancients:")
                        print("I have cities, but no houses.")
                        print("I have mountains, but no trees.")
                        ans=(input("I have water, but no fish.\nWho Am I ? Type map or not map "))
                        if ans !="map" and ans !="not map":
                            print("Invalid input")
                        else:
                            if ans=="map":
                                print("\n🎉 Correct! You have proven your wisdom.")
                                print("The treasure is yours! You win the game and become a legendary adventurer! 🏆")
                            else:
                                print("\n💀 Wrong answer!")
                                print("The walls close in and a trapdoor opens beneath your feet...")
                                print("You fall into a pit of darkness. Game Over.")
                    elif color=="red":
                        print("You open the red door and see a dark room with a red light.")
                        print("A voice says: 'Answer my question to get the treasure, or you will burn.'")
                        print("Riddle: The more you take, the more you leave behind. What am I?")
                        print("A. footsteps")
                        print("B. time")
                        print("C. money")
                        answer = input("Type your answer: ")
                        if answer !="footsteps" and answer !="time" and answer !="money":
                            print("Invalid input")
                        else:
                            if answer == "footsteps":
                                print("Correct! You solved the riddle.")
                                print("A secret door opens and you find the treasure. 🎉 You win!")
                            else:
                                print("Wrong answer!")
                                print("The room catches fire and burns you.")
                                print("🔥 Burned by fire. Game Over.")
                    else:
                        ans=input("You open a blue gate.\nType left or right one side is secure ")
                        if ans !="left" and ans!="right":
                            print("Invalid input")
                        else:
                            if ans=="right":
                                print("There are wild animals ")
                                print("Eaten by animal ")
                                print("Game over")
                            else:
                                print("You choose the left path")
                                print("It's dark and you can't see anything!")
                                action=input("you can do one thing light torch or go blind ")
                                if action!="light torch" and action!="go blind":
                                    print("Invalid input")
                                else:
                                    if action=="light torch":
                                        print("torch brighten everything \nThere is a pond and after crossing a pond there is a room")
                                        cross = input("How do you cross the pond? Type 'build' to build a raft, 'fly' to swing across ")
                                        if cross!="build" and cross != "fly":
                                            print("Invalid input")
                                        else:
                                            if cross=="build":
                                                print("You gather the wooods and create a raft")
                                                print("Reaches to the room\n🎉Found the treasure game over")
                                            else:
                                                print("You swing throug the room there is a shark inside the pond ")
                                                print("When swinging shark detected you and eaten by the shark")
                                    else:
                                        print("You bravely walk into the darkness...")
                                        print("Suddenly you slip and fall into a pit. 💀 Game Over.")
            else:
                print("Eaten by beasts.\nGame over")
    else:
        print("Fall into a hole.\nGame over")


