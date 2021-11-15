import random
def compare_numbers():
    npc_number = random.randint(1,25)
    player_guess = None
    attempts = 0
    out_of_guesses = False

    while player_guess != npc_number and not out_of_guesses:
        if attempts < 5:
            player_guess = int(input("Choose a number between 1 and 25\n"))
            if player_guess < npc_number:
                attempts +=1
                print("Your choice was too low - guess again!")
            elif player_guess > npc_number:
                attempts +=1
                print("Your choice was too high - guess again!")
            else:
                print(f"Congrats! You guessed {npc_number} correctly. Please grab a COOKIE!")
        else:
            print("You lost! Try again!")
            out_of_guesses = True
            compare_numbers()
            break



compare_numbers()

