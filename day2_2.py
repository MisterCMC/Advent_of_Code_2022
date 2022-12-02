from sys import argv
script, input = argv

data = open(input).read()
data_lst = data.split('\n')

def convert(move):
    if move == 'A':
        return 1
    elif move == 'B':
        return 2
    elif move == 'C':
        return 3
    elif move == 'X':
        return 0
    elif move == 'Y':
        return 3
    elif move == 'Z':
        return 6

total_score = 0
for i in range(0, len(data_lst)-1):
    play = data_lst[i].split(' ')
    their_move = convert(play[0])
    outcome = convert(play[1])
    total_score += outcome
    if outcome == 3:
        total_score += their_move
    elif outcome == 0:
        my_move = their_move - 1
        if my_move == 0:
            my_move += 3
        total_score += my_move
    elif outcome == 6:
        my_move = their_move + 1
        if my_move == 4:
            my_move += -3
        total_score += my_move
print(total_score)
