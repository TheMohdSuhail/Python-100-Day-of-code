import random


while True:
    choices = ["rock", "scissors", "paper"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors? : ").lower()

    if player == computer:
        print("computer : ", computer)
        print("player : ", player)
        print("Tie!")

    elif player =="rock":
        if computer =="paper":
            print("computer : ", computer)
            print("player : ", player)
            print("You Lose!")
        if computer =="scissors":
            print("computer : ", computer)
            print("player : ", player)
            print("You Win!")
    elif player =="scissors":
        if computer =="rock":
            print("computer : ", computer)
            print("player : ", player)
            print("You Lose!")
        if computer =="paper":
            print("computer : ", computer)
            print("player : ", player)
            print("You Win!")

    elif player =="paper":
        if computer =="rock":
            print("computer : ", computer)
            print("player : ", player)
            print("You win!")
        if computer =="scissors":
            print("computer : ", computer)
            print("player : ", player)
            print("You lose!")        
    play_again = input("play again? (yes/no) : ").lower()

    if play_again !="yes":
        break

print("Bye!")
    
