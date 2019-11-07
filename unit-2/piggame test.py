import random

player1_total = 0
player2_total = 0
player1_score = 0
player2_score = 0
player_total = 0
winning_total = 20

select_player = input ('Select the player_1 or player_2')
dice_roll = input('Roll the dice enter r or hold it enter h')

#r = random.randint(0,5)


while player_total < 20:
    if dice_roll == 'r' and select_player =='player_1':
        r = random.randint(0,6)
        player1_score += r
    elif dice_roll == 'h' and select_player =='player_1':
        r = random.randint(0,6)
        player1_score += r
    elif dice_roll == 'r' and select_player =='player_2':
        r = random.randint(0,6)
        player2_score += r
    else:
        r = random.randint(0,6)
        player_score += r
print(player1_total)

        


