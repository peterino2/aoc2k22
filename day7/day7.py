
import re
f = [line.strip('\n') for line in open("day7.input").readlines()]

dirs = {}
sum = 0
current_dir = None
parents = []
total_path = ""

def get_total_current_path():
    global current_dir
    global parents
    return "/".join(parents[1:]) + "/"

for line in f:
    if line.startswith("$ cd"):
        next_dir = line[5:]
        if next_dir == '..':
            if parents[-1] == None:
                continue
            next_dir = parents[-1]
            parents = parents[:-1]
        else:
            parents.append(current_dir)
        current_dir = next_dir
        sum = 0
        if current_dir not in dirs:
            dirs[current_dir] = 0
        print(line, ":::", current_dir, parents)

    x = re.findall(r"(\d+) (.+)", line)
    if x:
        dirs[current_dir] += int(x[0][0])
        for parent in parents:
            if parent is not None:
                dirs[parent] += int(x[0][0])


def get_total_dir_size(dirname): 
    global dirs
    sum = dirs[dirname]
    return sum

print(dirs)

total = 0
for dir in dirs:
    d = get_total_dir_size(dir)
    if d < 100000:
        total += d

print("total: ", total)
