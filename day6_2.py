from sys import argv
script, input = argv

transmission = open(input).read()

for i in range(0, len(transmission)):
    flag = True
    marker = transmission[i-14:i]
    if marker == '':
        continue
    score = []
    for j in range(0, 14):
        score.append(ord(marker[j]))
    for k in range(0, 14):
        numbers = list(range(k+1, 14))
        for number in numbers:
            if score[k] - score[number] == 0:
                flag = False
    if flag == False:
        continue
    elif flag == True:
        print(i)
        break
