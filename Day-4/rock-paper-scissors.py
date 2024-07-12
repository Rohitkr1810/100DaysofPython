import random

user_choice = int(input("What do you choose?\n0 for ROCK, 1 for PAPER or 2 for SCISSORS\n"))

#0 > 2
#1 > 0
#2 > 1

computer_choice = random.randint(0,2)

rock_paper_scissors =['ROCK','PAPER','SCISSORS']

print(f"You choose {rock_paper_scissors[user_choice]}")
print(f"Computer choose {rock_paper_scissors[computer_choice]}")

if user_choice != computer_choice :
    if user_choice ==0 and computer_choice == 2:
        print("You Win")
    elif user_choice == 1 and computer_choice == 0:
        print("You Win")
    elif user_choice == 2 and computer_choice ==1:
        print("You Win")
    else:
        print("You lose")
elif user_choice>=3:
    print("With Great Power Comes Great Responsibility")
    print("Make a valid choice")
else:
    print("Its a draw")