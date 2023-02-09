# 09-01-21
# NATE, NIKKA C.
# REGALA, JHON RAYMOND S.
# CCS 1101 - CSAA
# JACK 'EN POY

print("JACK 'EN POY")

# Player one inputs
print("Player one: Select your option")
print("[1] Paper")
print("[2] Rock")
print("[3] Scissors")
player_one = int(input("Player one input: "))

# invalid input for player one
if player_one <= 0 or player_one >= 4:
    print("Input error. Please enter a valid player two input.")
# Player two inputs
else:
    print("Player two: Select your option")
    print("[1] Paper")
    print("[2] Rock")
    print("[3] Scissors")
    player_two = int(input("Player two input: "))
    
    #invalid input for player two
    if player_one <= 0 or player_one >= 4:
        print("Input error. Please enter a valid player two input.")
    # prints player one and two inputs
    else:
        print(" Player one input: {0:,}.".format(player_one))
        print(" Player two input: {0:,}.".format(player_two))
        
        # paper vs paper
        if player_one == 1 and player_two == 1:
            print(" Its a draw. Nobody wins.")
        # paper vs rock
        elif player_one == 1 and player_two == 2:
            print(" Player one wins. ")
        # paper vs scissor
        elif player_one == 1 and player_two == 3:
            print(" Player two wins. ")
        # rock vs rock
        elif player_one == 2 and player_two == 2:
            print(" Its a draw. Nobody wins.")
        # rock vs paper
        elif player_one == 2 and player_two == 1:
            print(" Player two wins.")
        # rock vs scissor
        elif player_one == 2 and player_two == 3:
            print(" Player one wins.")
        # scissor vs scissor
        elif player_one == 3 and player_two == 3:
            print(" Its a draw. Nobody wins.")
        # scissor vs paper
        elif player_one == 3 and player_two == 1:
            print(" Player one wins.")
        # scissor vs rock
        elif player_one == 3 and player_two == 2:
            print(" Player two wins.")
        else:
            print(" \nInput error. Please enter a valid player two input.")
