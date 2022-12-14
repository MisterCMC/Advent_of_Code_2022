from sys import argv
import numpy as np
import time
script, input = argv
start_time = time.time()

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
cave = np.zeros((y_dim+2, 1000))


# draw cave
for wall in coordinates:
    for j in range(0, len(wall)-1):
        start = (wall[j][0], wall[j][1])
        end = (wall[j+1][0], wall[j+1][1])
        distance = np.subtract(end, start)
        magnitude = np.sqrt(distance[0]**2 + distance[1]**2)
        unit_distance = (int(distance[0]/magnitude), int(distance[1]/magnitude))
        for k in range(0, int(magnitude)+1):
            point = np.add(start, np.dot(unit_distance, k))
            cave[point[1]][point[0]] = 2
for x in range(0, 1000):
    cave[y_dim+1][x] = 2

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
sand_start = (500, 0)
sand_fall = [(0,1), (-1,1), (1,1)]
flag = True
score = 0
while flag == True:
    sand_pos = sand_start
    if cave[0, 500] == 1:
        flag = False
    while sand_pos[1] < y_dim+2:
        for i in range(0, 3):
            new_sand_pos = np.add(sand_pos, sand_fall[i])
            if check_bounds(new_sand_pos, 1000, y_dim+2) == False:
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
            score += 1
            break

score = 0
for x in range(0, 1000):
    for y in  range(0, y_dim+2):
        if cave[y][x] == 1:
            score += 1
print(score)
print(time.time() - start_time)



