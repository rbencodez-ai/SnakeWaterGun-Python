import random


def main_menu():
    print("""====================================
     🐍 Snake, 💧 Water, 🔫 Gun
====================================
1. View Game Rules
2. Register Single Player
3. Register Multiplayer
4. Play Single Player Game
5. Play Multiplayer Game
6. Exit
====================================""")


def game_rules():
    print("""========= GAME RULES =========
1. The game has three possible moves:
   🐍 Snake (S)
   💧 Water (W)
   🔫 Gun (G)

2. Winning Conditions:
   • Snake drinks water → Snake wins
   • Water douses gun → Water wins
   • Gun shoots snake → Gun wins

3. If both players choose the same move → It's a tie.

4. Game Modes:
   • Single Player → You play against the computer.
   • Multiplayer → Player 1 vs Player 2.

5. Input Rules:
   • Type 'S' for Snake, 'W' for Water, 'G' for Gun.
   • Any invalid input will ask you to enter again.

6. Scoring:
   • Each win gives 1 point to the winner.
   • Tie → No points are given.
   • Final score decides the overall winner.

7. You can quit the game anytime from the menu.
==============================""")


game_characters = {
    "s": "Snake",
    "w": "Water",
    "g": "Gun"
}

win_map = {
    "s": "w",  # Snake beats Water
    "w": "g",  # Water beats Gun
    "g": "s"   # Gun beats Snake
}

player_name = ""
first_player_name = ""
second_player_name = ""


def single_player_details():
    print("\nRegister Single Player\n")
    global player_name
    player_name = input("Enter your name: ").strip()

    try:
        gender = input("Enter your Gender: ").strip()
        age = int(input("Enter your age: ").strip())

        if gender.lower() != "male" and gender.lower() != "female":
            raise Exception("Invalid Gender!")
        elif age < 0:
            raise Exception("Invalid Age")
    except Exception as e:
        print(f"Error: {e}")
    else:
        with open("single_player_details.txt", "a") as game_player_data_file:
            game_player_data_file.write(f"Player Name: {player_name}\n")
            game_player_data_file.write(f"Player Gender: {gender}\n")
            game_player_data_file.write(f"Player Age: {age}\n\n")

        print(f"\n✅ {player_name} registered successfully.\n")


def single_player_game():
    player_score = 0
    computer_score = 0
    round_num = 0

    while True:
        round_num += 1
        print(f"\nRound {round_num}\n")
        print("Enter 'S' 🐍 for Snake, 'W' 💧 for Water, and 'G' 🔫 for Gun")

        user_choice = input(f"{player_name} Choice: ").strip().lower()
        player_choices = "swg"
        computer_choice = random.choice(player_choices)

        if user_choice not in player_choices:
            print("\nInvalid choice! Please enter S, W, or G.")
            continue

        print(f"{player_name} Chose: {game_characters[user_choice]}")
        print(f"Computer Chose: {game_characters[computer_choice]}")

        if computer_choice == user_choice:
            print("It's a Draw!")
        else:
            if win_map[user_choice] == computer_choice:
                print(f"{player_name} Wins!")
                player_score += 1
            elif win_map[computer_choice] == user_choice:
                print("Computer Wins!")
                computer_score += 1

        choice = input("\nDo you want to play another round? (y/n): ").lower()
        if choice != 'y':
            break

    print("\n🏆 Final Scores:")
    print(f"{player_name} Score: {player_score}")
    print(f"Computer Score: {computer_score}")

    if player_score > computer_score:
        print(f"🎯 {player_name} Wins the Match!")
    elif computer_score > player_score:
        print("🎯 Computer Wins the Match!")
    else:
        print("🤝 The Match is a Tie!")

    with open("single_player_score_card.txt", "a") as f:
        f.write(f"Single Player - {player_name}: {player_score}, Computer: {computer_score}\n")

    print("\nReturning to Main Menu...\n")


def multi_players_detail():
    print("\nRegister First Player!\n")
    global first_player_name, second_player_name

    first_player_name = input("Player Name: ").strip()
    try:
        first_player_gender = input("Player Gender: ").strip()
        first_player_age = int(input("Player Age: ").strip())

        if first_player_gender.lower() != "male" and first_player_gender.lower() != "female":
            raise Exception("Invalid Gender!")
        elif first_player_age < 0:
            raise Exception("Invalid Age")
    except Exception as e:
        print(f"Error: {e}")
    else:
        with open("multi_players_data.txt", "a") as game_multi_player_data_file:
            game_multi_player_data_file.write(f"{first_player_name} Data\n")
            game_multi_player_data_file.write(f"Name: {first_player_name}\n")
            game_multi_player_data_file.write(f"Gender: {first_player_gender}\n")
            game_multi_player_data_file.write(f"Age: {first_player_age}\n\n")

        print(f"\n✅ {first_player_name} registered successfully.\n")

    print("\nRegister Second Player!\n")
    second_player_name = input("Player Name: ").strip()
    try:
        second_player_gender = input("Player Gender: ").strip()
        second_player_age = int(input("Player Age: ").strip())

        if second_player_gender.lower() != "male" and second_player_gender.lower() != "female":
            raise Exception("Invalid Gender!")
        elif second_player_age < 0:
            raise Exception("Invalid Age")
    except Exception as e:
        print(f"Error: {e}")
    else:
        with open("multi_players_data.txt", "a") as game_multi_player_data_file:
            game_multi_player_data_file.write(f"{second_player_name} Data\n")
            game_multi_player_data_file.write(f"Name: {second_player_name}\n")
            game_multi_player_data_file.write(f"Gender: {second_player_gender}\n")
            game_multi_player_data_file.write(f"Age: {second_player_age}\n\n")

        print(f"\n✅ {second_player_name} registered successfully.\n")


def multi_player_game():
    first_player_score = 0
    second_player_score = 0
    round_num = 0
    player_choices = "swg"

    while True:
        round_num += 1
        print(f"\nRound {round_num}\n")
        print("Enter 'S' 🐍 for Snake, 'W' 💧 for Water, and 'G' 🔫 for Gun")

        first_player = input(f"Enter the choice of {first_player_name}: ").strip().lower()
        second_player = input(f"Enter the choice of {second_player_name}: ").strip().lower()

        if first_player not in player_choices or second_player not in player_choices:
            print("\nInvalid choice! Please enter S, W, or G.")
            continue

        print(f"{first_player_name} Chose: {game_characters[first_player]}")
        print(f"{second_player_name} Chose: {game_characters[second_player]}")

        if first_player == second_player:
            print("It's a Draw!")
        else:
            if win_map[first_player] == second_player:
                print(f"{first_player_name} Wins!")
                first_player_score += 1
            elif win_map[second_player] == first_player:
                print(f"{second_player_name} Wins!")
                second_player_score += 1

        choice = input("\nDo you want to play another round? (y/n): ").lower()
        if choice != 'y':
            break

    print("\n🏆 Final Scores:")
    print(f"{first_player_name} Score: {first_player_score}")
    print(f"{second_player_name} Score: {second_player_score}")

    if first_player_score > second_player_score:
        print(f"🎯 {first_player_name} Wins the Match!")
    elif second_player_score > first_player_score:
        print(f"🎯 {second_player_name} Wins the Match!")
    else:
        print("🤝 The Match is a Tie!")

    with open("multiple_player_score_card.txt", "a") as f:
        f.write(f"Multiplayer Game Player - {first_player_name}: {first_player_score}, {second_player_name}: {second_player_score}\n")

    print("\nReturning to Main Menu...\n")


while True:
    main_menu()
    try:
        user_choice = int(input("Enter the numbers to perform the above operations: "))
        if user_choice < 1 or user_choice > 6:
            raise Exception("Invalid Options!")
    except Exception as e:
        print(f"Error: {e}")
    else:
        if user_choice == 1:
            game_rules()
        elif user_choice == 2:
            single_player_details()
        elif user_choice == 3:
            multi_players_detail()
        elif user_choice == 4:
            single_player_game()
        elif user_choice == 5:
            multi_player_game()
        elif user_choice == 6:
            print("\nThanks for playing! Goodbye 👋\n")
            break