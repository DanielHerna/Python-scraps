x = 15
y = 20
z = 5

if x > 5:
    print(f"{x} is greater than 5")
elif x == 1:
    print(f"{x} is equal to 1")
else:
    print(f"{x} is less than 5")


if x>10 and y>15:
    print(f"{x} is greated that 10 AND {y} is greater than 20")


if x>10 or z>20:
    print(f"{x} is greated that 10 OR {z} is greater than 20")

''' ------------- Rock, Paper, Scissors challenge -------------'''
print("---------- Welcome to the game ----------")

player_1 = input("Player 1 - Type your movement: ").lower()
player_2 = input("Player 2 - Type your movement: ").lower()

valid_moves = ["rock","paper","scissors"]

while player_1 not in valid_moves or player_2 not in valid_moves:
    print("One of the players did an invalid move")
    player_1 = input("Player 1 - Select between rock, paper, and scissors: ").lower()
    player_2 = input("Player 2 - Select between rock, paper, and scissors: ").lower()

if player_1==player_2:
    print("There is a tie")
elif player_1==valid_moves[0] and player_2==valid_moves[1] or player_1==valid_moves[1] and player_2==valid_moves[2] or player_1==valid_moves[2] and player_2==valid_moves[0]:
    print("player 2 wins")
else:
    print("Player 1 wins")

print("---------- End of the game ----------")

