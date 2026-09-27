from random import randint
computer = randint(1,100)

user = -1
gusses = 1

while (user != computer):
    gusses += 1
    user = int(input("Guess number 1 to 100 :  "))
    if(user>computer):
        print("lower number Please")
    elif(user<computer):
        print("Higher number Please")

    else:    
        print(f"You Gusse right number : {user}\nyou count of gusses is {gusses} ") 