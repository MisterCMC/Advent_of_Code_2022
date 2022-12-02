from sys import argv
script, input = argv

data = open(input).read()
data_lst = data.split('\n')

def convert(move):
    if move == 'A' or move == 'X':
        return 1
    if move == 'B' or move == 'Y':
        return 2
    if move == 'C' or move == 'Z':
        return 3

total_score = 0
for i in range(0, len(data_lst)-1):
    play = data_lst[i].split(' ')
    their_move = convert(play[0])
    my_move = convert(play[1])
    total_score += my_move
    if their_move == my_move:
        total_score += 3
        continue
    elif (my_move > their_move and (my_move + their_move) % 2 == 1) or (my_move < their_move and (my_move + their_move) % 2 == 0):
        total_score += 6
        continue
    else:
        continue
print(total_score)
