import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions:")
    print("- Type 'rock', 'paper', or 'scissors' to play.")
    print("- Type 'quit' to exit the game.\n")

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice == "quit":
            print("\nGame over!")
            print(f"Final Scores -> You: {user_score}, Computer: {computer_score}")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.\n")
            continue

        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Scores -> You: {user_score}, Computer: {computer_score}\n")

if __name__ == "__main__":
    main()