import numpy as np
from sys import argv
script, input = argv

raw_data = open(input).read()
data = raw_data.split('\n')
forest = np.zeros([len(data[0]), len(data)-1])

for i in range(0, len(data)-1):
    for j in range(0, len(data[0])):
        forest[i][j] = data[i][j]

visible_trees = 0
for x in range(0, len(data)-1):
    for y in range(0, len(data[0])):
        if x == 0 or x == len(data[0])-1:
            visible_trees += 1
            continue
        if y == 0 or y == len(data)-2:
            visible_trees += 1
            continue
        row = forest[x]
        column = forest[:,y]
        flag = True
        for i in range(0, y):
            if row[i] >= row[y]:
                flag = False
                continue
        if flag == True:
            visible_trees += 1
            continue
        flag = True
        for i in range(len(data[0])-1, y, -1):
            if row[i] >= row[y]:
                 flag = False
                 continue
        if flag == True:
            visible_trees += 1
            continue
        flag = True
        for i in range(0, x):
            if column[i] >= column[x]:
                 flag = False
                 continue
        if flag == True:
            visible_trees += 1
            continue
        flag = True
        for i in range(len(data)-2, x, -1):
            if column[i] >= column[x]:
                 flag = False
                 continue
        if flag == True:
            visible_trees += 1
            continue
print(visible_trees)
