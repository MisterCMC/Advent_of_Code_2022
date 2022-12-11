from sys import argv
from day11_class import Monkey
import queue as q
from math import trunc
script, input = argv

raw_data = open(input).read()
data = raw_data.split('\n\n')



monkeys = {}
for item in data:
    lines = item.split('\n')
    name = 'Monkey' + lines[0][7]
    monkeys[name] = Monkey(name)

    start_items_list = lines[1].split(':')
    start_items = start_items_list[1].split(',')
    for start in start_items:
        monkeys[name].queue_item(int(start))
    
    operation = lines[2].split('=')
    key = operation[1][5]
    number = operation[1][7:]
    monkeys[name].set_operation(key, number)
    
    test = lines[3].split('by')
    passed = lines[4].split('monkey')
    failed = lines[5].split('monkey')
    number = int(test[1][1:])
    monkeys[name].set_test(number, passed[1], failed[1])

i = 0   
while i < 20:
    i += 1
    for j in range(0, len(data)):
        name = 'Monkey' + str(j)
        for k in range(0, monkeys[name].queue_size()):
            worry = monkeys[name].get_item()
            inspection = monkeys[name].operate(worry)
            relax = int(trunc(inspection / 3))
            new_name = monkeys[name].testing(relax)
            monkeys[new_name].queue_item(relax)

inspections = []
for item in data:
    lines = item.split('\n')
    name = 'Monkey' + lines[0][7]
    inspections.append(monkeys[name].get_inspections())

scores = sorted(inspections)
monkey_business = scores[-1] * scores[-2]
print(monkey_business)



