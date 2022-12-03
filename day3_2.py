from sys import argv
script, input = argv

raw_data = open(input).read()
data_lst = raw_data.split('\n')

total_priority = 0
for i in range(0, len(data_lst)-1, 3):
    elf_one = set()
    for j in range(0, len(data_lst[i])):
        elf_one.add(data_lst[i][j])
    elf_two = set()
    for j in range(0, len(data_lst[i+1])):
        elf_two.add(data_lst[i+1][j])
    elf_three = set()
    for j in range(0, len(data_lst[i+2])):
        elf_three.add(data_lst[i+2][j])
    badge = (elf_one & elf_two & elf_three).pop()
    print(badge)
    priority = ord(badge)
    if priority > 95:
        total_priority += priority - 96
    elif priority < 95:
        total_priority += priority - 38
print(total_priority)
