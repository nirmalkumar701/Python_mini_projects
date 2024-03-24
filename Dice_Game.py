import random

# assigning palyer default values
player1_ts=0
player2_ts=0

# Looping for 10 rounds
for i in range(1,11):
    print("****Round {}******".format(i))
    need1=input("Player1 Press Enter to roll dice ")
    player1_s=random.randint(1,6)
    print("Number {}".format(player1_s))
    need2=input("Player2 Press Enter to roll dice ")
    player2_s=random.randint(1,6)
    print("Number {}".format(player2_s))

    if player1_s>player2_s:
        player1_ts = player1_ts+1
        print("Player1 total score={}".format(player1_ts))
        print("Player2 total score={}".format(player2_ts))
        print("Player1 won this round")
        
    elif player1_s<player2_s:
        player2_ts =player2_ts+ 1
        print("Player2 total score={}".format(player2_ts))
        print("Player1 total score={}".format(player1_ts))
        print("Player2 won this round")
    else:
        print("This round is draw")
if player1_ts > player2_ts:
    print("Player1 won this match")
elif player1_ts < player2_ts:
    print("Player1 won this match")
else:
    print("This match is draw")
