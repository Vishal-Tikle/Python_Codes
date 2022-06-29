import random

v = 1
while v == 1:
    choices= [ "rock","paper","scissor"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        print("-----------------------------------")
        player = input(" rock , paper or scissor : ")
        player = player.lower()
    else:
        print("-----------------------------------")
        print(" Computer\t: ",computer)
        print(" Player\t\t: ",player)
        print("-----------------------------------")
        
    if computer == player :
        print("\t\tTie ! ")
    elif player == "rock":
        if computer == "paper":
            print("\t  You lose ! ")
        else:
            print("\t  You win ! ")
    elif player == "paper":
        if computer == "rock":
            print("\t  You win ! ")
        else:
            print("\t  You lose ! ")
    elif player == "scissor":
        if computer == "paper":
            print("\t  You win ! ")
        else:
            print("\t  You lose ! ")
    print("-----------------------------------\n")
    v=int(input(" Do you want to continue....press 1 : "))