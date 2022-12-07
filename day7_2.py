from sys import argv
from day7_class import Directory
from day7_class import File
import queue
script, input = argv

raw_data = open(input).read()
data = raw_data.split('\n')

def define_type(line):
    if line == '':
        return None
    elif line[0:4] == '$ ls':
        return None
    elif line[0:4] == '$ cd':
        return line[5:]
    else:
        file = line.split(' ')
        return file


new_data = []
duplicate = {}
for i in range(0, len(data)):
    line = data[i]
    if line[0:4] == '$ cd':
        if line[5:] in duplicate:
            new_line = line + duplicate[line[5:]][-1]
            if len(duplicate[line[5:]]) > 1:
                duplicate[line[5:]] = duplicate[line[5:]][0:-1]
            else:
                del duplicate[line[5:]]
        else:
            new_line = line + str(i)
    elif line[0:3] == 'dir':
        new_line = line + str(i)
        if line[4:] in duplicate:
            duplicate[line[4:]].append(str(i))
        else:
            duplicate[line[4:]] = [str(i)]
    elif line == '':
        new_line = line
    else:
        new_line = line + str(i)
    new_data.append(new_line)

dir = {}
dir_history = queue.LifoQueue()
current_dir = '\\'
for i in range(0, len(new_data)):
    line = new_data[i]
    dir_name = define_type(line)
    if type(dir_name) is str:
        if dir_name[0:2] == '..':
            moving = dir_history.get()
            current_dir = dir_history.queue[-1]
        else:
            flag = False
            if i == 0:
                dir[dir_name] = Directory(dir_name)
                dir_history.put(dir_name)
                current_dir = dir_history.queue[-1]
                continue
            sub_dirs = dir[current_dir].get_subdir()
            for sub in sub_dirs:
                new_sub = ''.join((x for x in sub if not x.isdigit()))
                new_dir = ''.join((x for x in dir_name if not x.isdigit()))
                if new_sub == new_dir:
                    dir[sub] = Directory(sub)
                    flag = True
            if flag == False:
                dir[dir_name] = Directory(dir_name)
            dir_history.put(dir_name)
            current_dir = dir_history.queue[-1]
    elif type(dir_name) is list:
        if dir_name[0] == 'dir':
            sub_dir = dir_name[1]
            dir[current_dir].add_dir(sub_dir)
        else:
            file_name = dir_name[1]
            file_size = int(dir_name[0])
            dir[current_dir].add_file(file_name, file_size)

score = 0
summed_dirs = set()
all_dirs = set()
for item in dir:
    all_dirs.add(dir[item].get_name())
while True:
    for item in dir:
        if dir[item].get_name() in summed_dirs:
            continue
        #print('\n')
        #print(dir[item].get_name())
        sub_dirs = dir[item].get_subdir()
        if sub_dirs == []:
            summed_dirs.add(dir[item].get_name())
        flag = True
        for sub in sub_dirs:
            if sub not in summed_dirs:
                flag = False
        if flag == False:
            continue
        for sub in sub_dirs:
            extra_size = dir[sub].get_size()
            dir[item].add_size(extra_size)
            summed_dirs.add(dir[item].get_name())
        #print(all_dirs.difference(summed_dirs))
        #print('\n')
    if summed_dirs == all_dirs:
        break

overall_size = dir['/0'].get_size()
remaining_space = 70000000 - overall_size
min_target = 30000000 - remaining_space
best_size = 70000000
best_dir = 0
for key in dir:
    current_size = dir[key].get_size()
    if current_size < min_target:
        continue
    else:
        score = current_size - min_target
        if score < best_size:
            best_size = score
            best_dir = current_size
print(best_dir)
