from sys import argv
script, input = argv

raw_data = open(input).read()
instructions = raw_data.split('\n')

cycles = 1
X = 1
checkpoint = 20, 60, 100, 140, 180, 220
flag = False
i = 0
score = 0
while i < len(instructions):
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
    if cycles in checkpoint:
        strength = cycles * X
        score += strength
print(score)