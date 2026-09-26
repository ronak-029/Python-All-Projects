import random

pick = ["rock", "paper" , "scissors"]

user = input("Enter Your Choise :")
computer = random.choice(pick)


print(f"this is user choice : {user}")
print(f"this is computer choice : {computer}")

if user == computer:
    print("It's a tie!")

elif user == "rock" and computer == "scissors":
    print("You win!")

elif user == "paper" and computer == "rock":
    print("You win!")

elif user == "scissors" and computer == "paper":
    print("You win!")

elif user in  choice :
    print("Computer wins!")

else:
    print("Invalid choice!")

    