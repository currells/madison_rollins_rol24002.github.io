"""create a simple game. create a class called player.  create 2 instances of that class and have them fight eachoter and keep track of their health."""
import random

class Player:
    def __init__(self, name, health):
        self.name = name
        health = 100
        self.health = health

    def attack(self, opponent):
        opponent.health -= random.randint(1, 10)
        return opponent.health
    
Player1 = Player("Player1", 100)
Player2 = Player("Player2", 100)    

print(f"{Player1.name} health: {Player1.health}")
print(f"{Player2.name} health: {Player2.health}")
print("")

while Player1.health > 0 and Player2.health > 0:

    print("")

    print(f"{Player1.name} attacks {Player2.name}")
    Player1.attack(Player2)
    print(f"{Player2.name} health: {Player2.health}")
    
    print("")

    print(f"{Player2.name} attacks {Player1.name}")
    Player2.attack(Player1)
    print(f"{Player1.name} health: {Player1.health}")

    print("")

if Player2.health <= 0:
    print(f"{Player1.name} wins!")
elif Player1.health <= 0:
    print(f"{Player2.name} wins!")