import random

option = [
    "rock","paper","scissors"
    ]

#Looping of the game
while True:
    human = input("Enter the option here please: ")
    if human == "rock":
        human_option = option[0]
    elif human == "paper":
        human_option = option[1]
    else:
       human_option = option[2]

    computer = random.randint(1,3)
    if computer == 1:
        computer_option = option[0]
    elif computer == 2:
        computer_option = option[1]
    else:
        computer_option = option[2]
#winning condition

    if human_option == computer_option:
        print(human_option + "<==Draw==>" + computer_option)
    elif human == "rock" or computer == 1:
        print("Winner ==> Computer")
        if human == option[1] or computer == option[0]:
            print("Winner ==> human")
    elif human == "paper" or computer == 3:
        print("Winner ==> Computer")
        if human == option[3] or computer == option[2]:
            print("Winner ==> human")
    elif human == "scissors" or computer == 1:
        print("Winner ==> Computer")
        if human == option[0] or computer == option[3]:
            print("Winner ==> human")
    

    
    

    
    