players = ['player 1 ', 'cpu ']
current_turn = 0 
run = 0
while players :
        current_player = players[current_turn]
        print(f"its :{current_player}'s turn ")

    
        current_turn = (current_turn + 1)% len(players)
# 
print(current_turn)