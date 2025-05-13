import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissor"])

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissor") or \
         (user == "scissor" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("🎮 Welcome to Rock, Paper, Scissor Game! 🎮\n")
    
    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = input("Choose rock, paper, or scissor: ").strip().lower()

        if user_choice not in ["rock", "paper", "scissor"]:
            print("❌ Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"🤖 Computer chose: {computer_choice}")
        print(f" You chose: {user_choice}")

        winner = get_winner(user_choice, computer_choice)

        if winner == "tie":
            print("⚖️ It's a tie!")
        elif winner == "user":
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ Computer wins this round!")
            computer_score += 1

        print(f"🔢 Score - You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\n🎉 Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("🏆 Congratulations! You won the game!")
            elif user_score < computer_score:
                print("😔 Computer won the game. Better luck next time!")
            else:
                print("🤝 It's a draw!")
            break

        round_number += 1 

# Start the game
play_game()
