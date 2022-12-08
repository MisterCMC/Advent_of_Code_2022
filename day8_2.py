import numpy as np
from sys import argv
script, input = argv

raw_data = open(input).read()
data = raw_data.split('\n')
forest = np.zeros([len(data[0]), len(data)-1])

for i in range(0, len(data)-1):
    for j in range(0, len(data[0])):
        forest[i][j] = data[i][j]

best_score = 0
for x in range(0, len(data)-1):
    for y in range(0, len(data[0])):
        row = forest[x]
        column = forest[:,y]
        north = 0
        south = 0
        east = 0
        west = 0
        ticker = 0
        for i in range(y-1, -1, -1):
            ticker += 1
            if row[i] >= row[y]:
                break
        west = ticker
        ticker = 0
        for i in range(y+1, len(data[0])):
            ticker += 1
            if row[i] >= row[y]:
                 break
        east = ticker
        ticker = 0
        for i in range(x-1, -1, -1):
            ticker += 1
            if column[i] >= column[x]:
                 break
        north = ticker
        ticker = 0
        for i in range(x+1, len(data)-1):
            ticker += 1
            if column[i] >= column[x]:
                 break
        south = ticker
        score = north * south * east * west
        if score > best_score:
            best_score = score
print(best_score)
