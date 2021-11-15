import random

choices = ["rock", "paper", "scissors", "lizard", "spock"]
npc_choice = random.choice(choices)

class Player:
    def __init__(self, option):
        self.__option = option

class Game:
    def __init__(self, player, npc):
        self.player = player
        self.npc = npc

    def game_start(self):
        if self.player == self.npc:
            print("It's a tie!")
        elif self.player == "rock":
            if self.npc == "paper" or self.npc == "spock":
                return print("You lose!")
            else:
                return print("You win!")
        elif self.player == "paper":
            if self.npc == "scissors" or self.npc == "lizard":
                return print("You lose!")
            else:
                return print("You win!")
        elif self.player == "scissors":
            if self.npc == "rock" or self.npc == "spock":
                return print("You lose!")
            else:
                return print("You win!")
        elif self.player == "lizard":
            if self.npc == "rock" or self.npc == "scissors":
                return print("You lose!")
            else:
                return print("You win!")
        elif self.player == "spock":
            if self.npc == "paper" or self.npc == "lizard":
                return print("You lose!")
            else:
                return print("You win!")

player_choice = input(f"Please chose between: \n{choices}\n ").lower()
print(f"You have chosen {player_choice}, the computer has chosen {npc_choice}.\n")
Game(player_choice, npc_choice).game_start()