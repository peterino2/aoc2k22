import re
f = [line.strip('\n') for line in open("day7.input").readlines()]

dirs = [] # Each 'dir' is just a single number that tracks it's size
currentDir = None # a dir is referenced via it's index in the dirs array
parents = [] # I also keep a list of the parents for whatever current directory we're in

for line in f:
    if line.startswith("$ cd"):
        next_dir = line[5:]
        if next_dir == '..' and len(parents) > 0:
            currentDir = parents.pop()
        else:
            if currentDir is not None:
                parents.append(currentDir)
            currentDir = len(dirs)
            dirs.append(0)

    x = re.findall(r"(\d+) (.+)", line)
    if x:
        dirs[currentDir] += int(x[0][0])
        for parent in parents:
            dirs[parent] += int(x[0][0])

dirs.sort()

print("part 1:", sum(d if d <= 100000 else 0 for d in dirs))
unused_space_needed = -((70000000 - 30000000) - (dirs[-1]))
for dir in dirs:
    if dir >= unused_space_needed:
        print("part 2:", dir)
        break
