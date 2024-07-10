print("!!!!!!!!!!Welcome to the treasuer Island your mission is to find the treasure!!!!!!!!!!!")
print("Lets start the game")
print("You have started moving straigt")
print("XXX You are at a cross road XXX")
choice_1 = input("Choose the direction (left of right): ").lower()
if choice_1 == "left":
    print("Good Choice!!!\nNow you reached a lake, pass this for next step")
    choice_2= input("Choice an action (swim or wait): ").lower()
    if choice_2 == "wait":
        print("!!! You have reached the last door !!!")
        choice_3 = input("Choose the right colored door to move to the treasure (red, green, blue): ").lower()
        if choice_3=="red":
            print("It is a room full of fire\n!!!GAME OVER!!!")
        elif choice_3=="blue":
            print("It is a door to ocean\n!!!GAME OVER!!!")
        elif choice_3 =="green":
            print("!!!! YOU WON !!!!")
            print("!!!! TREASURE IS ALL YOURS !!!!")
        else:
            print("You cannot choose, loooooooser\n!!! GAME OVER !!!")
    else:
        print("You were attacked by AquaMan\n!!!GAME OVER!!!")        
else:
    print("You fell into a deeeeeep holeee\n !!!GAME OVER!!!")