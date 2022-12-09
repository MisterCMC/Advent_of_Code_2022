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


h_coords = [0, 0]
old_h = h_coords
t_coords = [0, 0]
visited = set()
visited.add(tuple([0, 0]))
for inst in instructions:
    dir_dist = inst.split(' ')
    dir_str = dir_dist[0]
    dir = direction(dir_str)
    dist = int(dir_dist[1])
    for i in range(1, dist+1):
        old_h = list(h_coords)
        h_coords[0] += dir[0]
        h_coords[1] += dir[1]

        x_dist = abs(h_coords[0] - t_coords[0])
        y_dist = abs(h_coords[1] - t_coords[1])
        total_dist = x_dist + y_dist

        if total_dist == 2 and (x_dist == 0 or y_dist == 0):
            t_coords = old_h
            print(tuple(t_coords))
            visited.add(tuple(t_coords))
        elif total_dist == 2 and x_dist == 1:
            continue
        elif total_dist > 2 and (x_dist >=1 or y_dist >= 1):
            t_coords = old_h
            print(tuple(t_coords))
            visited.add(tuple(t_coords))
     
print(len(visited))

