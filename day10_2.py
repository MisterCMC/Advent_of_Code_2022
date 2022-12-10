from sys import argv
script, input = argv

raw_data = open(input).read()
instructions = raw_data.split('\n')

cycles = 1
X = 1
pixels = set()
flag = False
i = 0

while i < len(instructions):
    sprite = X-1, X, X+1
    pos = (cycles - 1) % 40
    if pos in sprite:
        pixels.add(cycles-1)
    inst = instructions[i].split(' ')
    if len(inst) == 1:
        cycles += 1
    elif len(inst) == 2 and flag == False:
        flag = True
        cycles += 1
    elif len(inst) == 2 and flag == True:
        X += int(inst[1])
        cycles += 1
        flag = False
    if flag == False:
        i += 1


image = []
for j in range(0, 6):
    image.append([])
    for k in range(0, 40):
        spot = k + j*40
        if spot in pixels:
            image[j].append('#')
        else:
            image[j].append('.')
for line in image:
    string = ''.join(line)
    print(string)

