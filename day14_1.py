from sys import argv
import numpy as np
import time
script, input = argv

raw_data = open(input).read()
data = raw_data.split('\n')

# initialise cave
smallest_x = 100000
largest_x = 0
y_dim = 0
coordinates = []
for i in range(0, len(data)):
    coords = data[i].split('->')
    coordinates.append([])
    for coord in coords:
        numbers = coord.split(',')
        coordinates[i].append((int(numbers[0]), int(numbers[1])))
        if int(numbers[0]) < smallest_x:
            smallest_x = int(numbers[0])
        if int(numbers[0]) > largest_x:
            largest_x = int(numbers[0])
        if int(numbers[1]) > y_dim:
            y_dim = int(numbers[1])+1

x_dim = 1 + largest_x - smallest_x
cave = np.zeros((y_dim, x_dim))

# draw cave
for wall in coordinates:
    for j in range(0, len(wall)-1):
        start = (wall[j][0] - smallest_x, wall[j][1])
        end = (wall[j+1][0] - smallest_x, wall[j+1][1])
        distance = np.subtract(end, start)
        magnitude = np.sqrt(distance[0]**2 + distance[1]**2)
        unit_distance = (int(distance[0]/magnitude), int(distance[1]/magnitude))
        for k in range(0, int(magnitude)+1):
            point = np.add(start, np.dot(unit_distance, k))
            cave[point[1]][point[0]] = 2

def check_bounds(pos, x_lim, y_lim):
    if pos[1] >= y_lim:
        return False
    elif pos[0] >= x_lim:
        return False
    elif pos[0] < 0:
        return False
    else:
        return True

# falling sand
sand_start = (500 - smallest_x, 0)
sand_fall = [(0,1), (-1,1), (1,1)]
flag = True
while flag == True:
    sand_pos = sand_start
    while sand_pos[1] < y_dim:
        for i in range(0, 3):
            new_sand_pos = np.add(sand_pos, sand_fall[i])
            if check_bounds(new_sand_pos, x_dim, y_dim) == False:
                flag = False
                sand_pos = new_sand_pos
                break
            if 1 - cave[new_sand_pos[1]][new_sand_pos[0]] <= 0:
                continue
            elif 1 - cave[new_sand_pos[1]][new_sand_pos[0]] == 1:
                sand_pos = new_sand_pos
                break
        if new_sand_pos[0] != sand_pos[0] or new_sand_pos[1] != sand_pos[1]:
            cave[sand_pos[1]][sand_pos[0]] = 1
            break

score = 0
for x in range(0, x_dim):
    for y in  range(0, y_dim):
        if cave[y][x] == 1:
            score += 1
print(score)



