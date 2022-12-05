import queue
from sys import argv
script, input = argv

raw_data = open(input).read()
data_split = raw_data.split('\n\n')
start_position = data_split[0].split('\n')
instructions = data_split[1].split('\n')

# Generate starting queues
piles = []
num_piles = int(start_position[-1][-1])
for i in range(0, num_piles):
    piles.append(queue.LifoQueue())
for i in range(len(start_position)-2, -1, -1):
    j = 1
    while j<=len(start_position[i]):
        cargo = start_position[i][j]
        if cargo == ' ':
            j += 4
            continue
        pos = int(((j + 3) / 4) - 1)
        piles[pos].put(cargo)
        j += 4

# Move cargo
for i in range(0, len(instructions)-1):
    instruction = instructions[i].split(' ')
    quantity = int(instruction[1])
    first_pos = int(instruction[3])-1
    final_pos = int(instruction[5])-1
    moving = queue.LifoQueue()
    for j in range(0, quantity):
        moving.put(piles[first_pos].get())
    for j in range(0, quantity):
        piles[final_pos].put(moving.get())

# Generate answer
top_crates = []
for i in range(0, len(piles)):
    top_crates.append(piles[i].get())
answer = ''.join(top_crates)
print(answer)
