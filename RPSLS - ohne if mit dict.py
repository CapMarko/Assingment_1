import random

choices = ["rock", "paper", "scissors", "lizard", "spock"]
player_choice = input(f"Please chose between {choices}\n").lower()
npc_choice = random.choice(choices)


def game_start():
    while True:
        print("Make your choice: ")
        print("My choice is", player_choice)
        print("Computer choice ist", npc_choice)

        choice_dict = {"rock": 0,
                       "paper": 1,
                       "scissors": 2,
                       "lizard": 3,
                       "spock": 4}

        player_choice_idx = choice_dict[player_choice]
        npc_choice_idx = choice_dict[npc_choice]
        print(player_choice_idx)
        print(npc_choice_idx)

        # generate all possible outcomes in a dict (0= tie, 1= win, 2= lose)
        # "rows" = player choices, "columns" = npc choises
        # e.g.: player_choice[1] ("row"), npc_choice[2] ("columns") --> reults = 2 = lose
        results = [[0, 2, 1, 1, 2],
                   [1, 0, 2, 2, 1],
                   [2, 1, 0, 1, 2],
                   [2, 1, 2, 0, 1],
                   [1, 2, 1, 2, 0]]
        results_idx = results[player_choice_idx][npc_choice_idx]
        print(results_idx)

        # result of game gives an index 0,1,2 --> using index to get result msg
        result_msg = ["it's a tie", "You win!", "You lose!"]
        result = result_msg[results_idx]
        print(result)
        break

game_start()