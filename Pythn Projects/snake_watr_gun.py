print("\t\t\t Snake, Water, Gun GAME !")

print("You Have 10 games to play with computer") 
# setting the inital scores as 0
player = 0
comp = 0
chance = 0
import  random
while(chance<10) :
    ch = str(input("\nEnter your choice\n1-Snake\n2-Water\n3-Gun\n"))
    if ch == "1" :
        list = ["Snake", "Water", "Gun"]
        compch = random.choice(list)
        if compch=="Snake" :
            print("Computer's choice : ", compch)
            print("This round is a tie")
        elif compch=="Water" :
            print("Computer's choice : ", compch)
            print("Snake Drank Water. Therefore you won this round")
            player=player+1
        else :
            print("Computer's choice : Gun ")
            print("Gun shot the snake. Therefore Computer won this round")
            comp=comp+1
        print("Your score : ", player, "Computer's score : ", comp)
        chance=chance+1
    elif ch== "2":
        list = ["Snake", "Water", "Gun"]
        compch = random.choice(list)
        if compch == "Snake":
            print("Computer's choice : ", compch)
            print("Snake Drank Water. Therefore Computer won this round")
            comp=comp+1
        elif compch == "Water":
            print("Computer's choice : ", compch)
            print("This round is a tie")
        else:
            print("Computer's choice : Gun ")
            print("Gun sunk . Therefore You won this round")
            player=player+1
        print("Your score : ", player, "Computer's score : ", comp)
        chance=chance+1
    elif ch=="3" :
        list = ["Snake", "Water", "Gun"]
        compch = random.choice(list)
        if compch == "Snake":
            print("Computer's choice : ", compch)
            print("Gun shot the snake. Therefore You won this round")
            player = player + 1
        elif compch == "Water":
            print("Computer's choice : ", compch)
            print("Gun sunk . Therefore Computer Water this round")
            comp = comp + 1
        else:
            print("Computer's choice : Gun ")
            print("This round is a tie")
        print("Your score : ", player, "Computer's score : ", comp)
        chance=chance+1
    else :
        print("Invalid choice")
print("Total Player Score : ", player, "Total Computer Score : ", comp)
if player>comp :
    print("You won the game")
elif comp>player :
    print("Computer won the game")
else :
    print("The game got tied at same scores")
