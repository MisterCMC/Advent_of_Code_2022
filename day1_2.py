from sys import argv
script, in_file = argv

raw_data = open(in_file).read()
data = raw_data.split('\n\n')

first_calories = 0
second_calories = 0
third_calories = 0
for i in range(0, len(data)):
    cals_str = data[i]
    cals_lst = cals_str.split('\n')
    calories = 0
    for j in range(0, len(cals_lst)):
        if cals_lst[j] == '':
            continue
        food = int(cals_lst[j])
        calories = calories + food
    if calories > first_calories:
        if first_calories > second_calories:
            if second_calories > third_calories:
                third_calories = second_calories
            second_calories = first_calories
        elif first_calories > third_calories:
            third_calories = first_calories
        first_calories = calories
    elif calories > second_calories:
        if second_calories > third_calories:
            third_calories = second_calories
        second_calories = calories
    elif calories > third_calories:
        third_calories = calories
total_calories = first_calories + second_calories + third_calories
print(total_calories)
