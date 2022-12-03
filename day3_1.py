from sys import argv
script, input = argv

raw_data = open(input).read()
data_lst = raw_data.split('\n')

total_priority = 0
for i in range(0, len(data_lst)-1):
    backpack = data_lst[i]
    division = int(len(backpack)/2)
    first_compartment = set()
    for j in range(0, division):
        first_compartment.add(backpack[j])
    second_compartment = set()
    for j in range(division, len(backpack)):
        second_compartment.add(backpack[j])
    item = first_compartment.intersection(second_compartment).pop()
    priority = ord(item)
    if priority > 95:
        total_priority += priority - 96
    elif priority < 95:
        total_priority += priority - 38
print(total_priority)
