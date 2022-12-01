from sys import argv
script, in_file = argv

raw_data = open(in_file).read()
data = raw_data.split('\n\n')

max_calories = 0
for i in range(0, len(data)):
    cals_str = data[i]
    cals_lst = cals_str.split('\n')
    calories = 0
    for j in range(0, len(cals_lst)):
        if cals_lst[j] == '':
            continue
        food = int(cals_lst[j])
        calories = calories + food
    if calories > max_calories:
        max_calories = calories
print(max_calories)
