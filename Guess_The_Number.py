import random

player1=input("You are Player1 Please Enter Your Name:-\n")
player2=input("You are Player2 Please Enter Your Name:-\n")
number1=int(input("Enter the starting range:-\n"))
number2=int(input("Enter the ending range:-\n"))

secret_number = random.randint(number1,number2)
secret_number2 = random.randint(number1,number2)


trails_by_player1=0
trails_by_player2=0
print(f"{player1} turn start")
while True:
    player1_input=int(input("Please choose your Number:-\n"))
    if player1_input > secret_number:
        print("You choose greater number")
        trails_by_player1=trails_by_player1+1
        continue
    elif player1_input < secret_number:
        print("You choose lesser number")
        trails_by_player1 = trails_by_player1 + 1
        continue
    elif player1_input==secret_number:
        print(f"{player1} you guess the right number and You took {trails_by_player1} no of trails")
        break

print(f"Now {player2} turn start")

while True:
    player2_input=int(input("Please choose your Number:-\n"))
    if player2_input > secret_number2:
        print("You choose greater number")
        trails_by_player2=trails_by_player2+1
        continue
    elif player2_input < secret_number2:
        print("You choose lesser number ")
        trails_by_player2 = trails_by_player2 + 1
        continue
    elif player2_input==secret_number2:
        print(f"{player2} you guess the right number and You took {trails_by_player2} no of trails")
        break

if trails_by_player1 < trails_by_player2:
    print(f"{player1} you won you take less number of guesses.......Congrats")
elif trails_by_player1>trails_by_player2:
    print(f"{player2} you won you take less number of guesses.......Congrats")
elif trails_by_player1==trails_by_player2:
    print("Match Tied.............")
else:
    print("Something went wrong")


