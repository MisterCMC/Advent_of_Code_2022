from sys import argv
script, input = argv

raw_data = open(input).read()
pairs = raw_data.split()

def ranger(range):
    bounds = range.split('-')
    lower = int(bounds[0])
    upper = int(bounds[1])
    sections = set()
    k = lower
    while k <= upper:
        sections.add(k)
        k += 1
    return sections

total_score = 0
for pair in pairs:
    ranges = pair.split(',')
    range_one = ranger(ranges[0])
    range_two = ranger(ranges[1])
    overlap = range_one.intersection(range_two)
    if len(overlap) > 0:
        total_score += 1
print(total_score)
