import random

def play_game():
    user_score = 0
    computer_score = 0
    draws = 0

    while True:
        # Ask for user's choice
        user_choice = input("Enter your choice (rock, paper, or scissors), or 'q' to quit: ")

        if user_choice.lower() == 'q':
            break

        if user_choice.lower() not in ['rock', 'paper', 'scissors']:
            if user_choice.strip() == '':
                print("Please enter a choice!")
            else:
                print("Invalid choice! Please enter a valid choice.")
            continue

        # Generate computer's choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        # Compare choices and determine the winner
        if user_choice.lower() == computer_choice:
            print("It's a draw!")
            draws += 1
        elif (
            (user_choice.lower() == 'rock' and computer_choice == 'scissors') or
            (user_choice.lower() == 'paper' and computer_choice == 'rock') or
            (user_choice.lower() == 'scissors' and computer_choice == 'paper')
        ):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        # Display the current score
        print(f"Score: You {user_score}, Computer {computer_score}, Draws {draws}\n")

play_game()
