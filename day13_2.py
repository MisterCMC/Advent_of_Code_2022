from sys import argv
script, input = argv

raw_data = open(input).read()
data = raw_data.split('\n\n')
lines = []
for line in data:
    lines.append(line.split('\n')[0])
    lines.append(line.split('\n')[1])

def parse_signal(signal):
    signal_items = []
    digits = signal
    k = 1
    while k < len(digits):
        if digits[k] == ',':
            k += 1
            continue
        elif digits[k] == '[':
            short_list = parse_signal(digits[k:])
            signal_items.append(short_list[0])
            k += short_list[1]
        elif digits[k] == ']':
            return signal_items, k + 1
        else:
            if digits[k+1] == ',' or digits[k+1] == '[' or digits[k+1] == ']':
                signal_items.append(int(digits[k]))
                k += 1
            else:
                signal_items.append(int(digits[k] + digits[k+1]))
                k += 2
    return signal_items, k + 1

def check_order(left, right):
    if len(left) > len(right):
        longest = len(right)
    else:
        longest = len(left)
    for k in range(0, longest):
        left_type = type(left[k])
        right_type = type(right[k])
        if left_type == right_type and left_type == int:
            if left[k] < right[k]:
                return True
            elif left[k] > right[k]:
                return False
            else:
                continue
        elif left_type == right_type and left_type == list:
            result = check_order(left[k], right[k])
            if result == True:
                return True
            elif result == False:
                return False
            else:
                continue
        else:
            if left_type == int:
                proxy_left = []
                proxy_left.append(left[k])
                proxy_right = right[k]
            elif right_type == int:
                proxy_right = []
                proxy_right.append(right[k])
                proxy_left = left[k]
            result = check_order(proxy_left, proxy_right)
            if result == True:
                return True
            elif result == False:
                return False
            else:
                continue
    if len(left) < len(right):
        return True
    elif len(left) > len(right):
        return False
    

correct_order = 1
for i in range(0, len(lines)):
    left = parse_signal('[[2]]')
    right = parse_signal(lines[i])
    result = check_order(left, right)
    if result == False:
        correct_order += 1

six_order = 2
for i in range(0, len(lines)):
    left = parse_signal('[[6]]')
    right = parse_signal(lines[i])
    result = check_order(left, right)
    if result == False:
        six_order += 1

print(correct_order * six_order)