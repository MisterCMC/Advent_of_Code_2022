from sys import argv
import numpy as np
import time
from day17_class import Rocks
script, input = argv
start_time = time.time()

#create instructions as tuples
raw_data = open(input).read()
gas = np.zeros(len(raw_data)*2, dtype=object)
for i in range(0, len(raw_data)*2):
    if i % 2 == 1:
        gas[i] = (0, -1)
    elif i % 2 == 0:
        j = int(i / 2)
        if raw_data[j] == '<':
            gas[i] = (-1, 0)
        elif raw_data[j] == '>':
            gas[i] = (1, 0)

#create rocks
rock = {}
rock_shape = [
    [(3,0), (4,0), (5,0), (6,0)],
    [(3,1), (4,1), (5,1), (4,2), (4,0)],
    [(3,0), (4,0), (5,0), (5,1), (5,2)],
    [(3,0), (3,1), (3,2), (3,3)],
    [(3,0), (3,1), (4,0), (4,1)]
    ]
for i in range(0, 5):
    rock[i] = Rocks(i,np.array(rock_shape[i], dtype=object))

# setup walls
chamber = set()
floor = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0)]
for i in range(0, 9):
    chamber.add(floor[i])

def generate_start(rock_shape, start_height):
    rock_height = rock_shape + start_height
    return rock_height

#drop rocks
num_rocks = 0
old_height = (0,0)
n = 0
while num_rocks <= 2021:
    id = num_rocks % 5
    start_height = (0, max(chamber, key=lambda x:x[1])[1] + 4)
    current_pos =  generate_start(rock[id].shaped, start_height)
    flag = True
    if n % 2 == 1:
        n += 1
    while flag == True:
        next_pos = current_pos + gas[n]
        next_pos_set = set()
        for i in range(0, len(next_pos)):
            next_pos_set.add((next_pos[i][0], next_pos[i][1]))
        if min(next_pos_set, key=lambda x:x[0])[0] == 0 or max(next_pos_set, key=lambda x:x[0])[0] == 8:
            n = (n + 1) % len(gas)
            continue
        clash = chamber.intersection(next_pos_set)
        if len(clash) == 0:
            n = (n + 1) % len(gas)
            current_pos = next_pos
            continue
        elif len(clash) > 0 and n % 2 == 0:
            n = (n + 1) % len(gas)
            continue
        else:
            n = (n + 1) % len(gas)
            for i in range(0, len(current_pos)):
                chamber.add((current_pos[i][0], current_pos[i][1]))
                flag = False
    old_height = start_height
    num_rocks += 1

print(max(chamber, key=lambda x:x[1])[1])
print(time.time() - start_time)