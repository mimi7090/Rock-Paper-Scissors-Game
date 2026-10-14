import random
choices = ["rock","paper","scissors"]
player_score = 0
computer_score = 0
while True :
    player = input("Enter your choice (rock/paper/scissors) :").lower()
    if player not in choices :
        print("Not a valid choice! Enter a valid choice :")
        continue
    computer = random.choice(choices)
    print("Your choice :",player)
    print("Computer choice :",computer)
    if player == computer :
        print("It's a tie")
    elif (player == "rock" and computer == "scissors") or \
        (player == "paper" and computer == "rock") or \
        (player == "scissors" and computer == "paper") :
        print("You win")
        player_score += 1
    else :
        print("Computer win!")
        computer_score += 1
    print("Your score :",player_score)
    print("Computer score :",computer_score)
    again = input("Play again (yes/no) :").lower()
    if again != "yes" :
        print("\n=====Final Score=====")
        print("Your score :",player_score)
        print("Computer score :",computer_score)
        if player_score > computer_score :
            print("You the game!")
        elif player_score < computer_score :
            print("Computer won the game!")
        else :
           print("The game ended in a Tie!")
        print("Thanks for playing!")
        break

    