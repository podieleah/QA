import random

def get_user_choice():
  while True:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if 0 <= user_choice <= 2:
      return user_choice
    else:
      print("Invalid choice. Please enter 0, 1, or 2.")

def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "Draw"
  elif (user_choice == 0 and computer_choice == 2) or \
       (user_choice == 1 and computer_choice == 0) or \
       (user_choice == 2 and computer_choice == 1):
    return "Win"
  else:
    return "Lose"

def play_game():
  user_score = 0
  computer_score = 0
  choices = ["Rock", "Paper", "Scissors"]

  while True:
    user_choice = get_user_choice()
    computer_choice = random.randint(0, 2)

    print(f"You chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")

    result = determine_winner(user_choice, computer_choice)
    print(result)


    if result == "Win":
      user_score += 1
    elif result == "Lose":
      computer_score += 1

    print(f"Score: You - {user_score}, Computer - {computer_score}")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
      break

play_game()