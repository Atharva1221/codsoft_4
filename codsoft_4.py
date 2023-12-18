#Rock-paper-scissor
#TASK-4
import random
print("----------Rock-Paper-scissor-----------")
def deter_winner(userchoice, pc_choice):
    if userchoice == pc_choice:
        return "It's a tie!"
    elif (userchoice == 'rock' and pc_choice == 'scissors') or \
         (userchoice == 'scissors' and pc_choice == 'paper') or \
         (userchoice == 'paper' and pc_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0
    choices = ['rock', 'paper', 'scissors']

    while True:
        userchoice = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()
        
        if userchoice == 'q':
            break
        
        if userchoice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        pc_choice = random.choice(choices)
        print(f"Computer chooses {pc_choice}")

        result = deter_winner(userchoice, pc_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        print(f"Your score: {user_score}, Computer's score: {computer_score}")
    
    print("Thanks for playing!!")

play_game()