from sys import argv
script, input = argv

raw_data = open(input).read()
instructions = raw_data.split('\n')

def direction(dir_str):
    if dir_str == 'R':
        return [1, 0]
    elif dir_str == 'L':
        return [-1, 0]
    elif dir_str == 'U':
        return [0, 1]
    elif dir_str == 'D':
        return [0, -1]

def check_sign(coord):
    if coord > 0:
        return 1
    if coord < 0:
        return -1
    if coord == 0:
        return 0


string_coords = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
old_string = [0, 0]
visited = set()
visited.add(tuple([0, 0]))
for inst in instructions:
    dir_dist = inst.split(' ')
    dir_str = dir_dist[0]
    dir = direction(dir_str)
    dist = int(dir_dist[1])
    for i in range(1, dist+1):
        flag = True
        old_string = list(string_coords[0])
        string_coords[0][0] += dir[0]
        string_coords[0][1] += dir[1]
        for j in range(1, 10):
            x_dist = abs(string_coords[j-1][0] - string_coords[j][0])
            y_dist = abs(string_coords[j-1][1] - string_coords[j][1])
            total_dist = x_dist + y_dist
            pos_copy = list(string_coords[j])
            if total_dist == 2 and (x_dist == 0 or y_dist == 0):
                x_change = check_sign((string_coords[j-1][0] - string_coords[j][0]))
                y_change = check_sign((string_coords[j-1][1] - string_coords[j][1]))
                string_coords[j][0] = pos_copy[0] + x_change
                string_coords[j][1] = pos_copy[1] + y_change
            elif total_dist == 2 and (x_dist == 1 and y_dist == 1):
                flag = True
                continue
            elif flag == True and total_dist == 3:
                flag = False
                string_coords[j] = list(old_string)
            elif flag == False and total_dist >= 3:
                x_change = check_sign((string_coords[j-1][0] - string_coords[j][0]))
                y_change = check_sign((string_coords[j-1][1] - string_coords[j][1]))
                string_coords[j][0] = pos_copy[0] + x_change
                string_coords[j][1] = pos_copy[1] + y_change
            if j == 9:
                visited.add(tuple(string_coords[9]))
            old_string = list(pos_copy)
print(len(visited))
