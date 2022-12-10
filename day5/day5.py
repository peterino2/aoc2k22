import re

# -- initialize stacks --
f = open("day5.input").readlines()
stackCount = 9
stackHeight = 8
stacks = [[] for i in range(stackCount)]
stacks2 = [[] for i in range(stackCount)]
lineCount = 0
for line in f:
    for idx in range(stackCount):
        ch = line[idx * 4 + 1]
        if(ch != ' '):
            stacks[idx].insert(0,ch)
            stacks2[idx].insert(0,ch)
    lineCount += 1
    if lineCount >= stackHeight:
        break
lineCount += 2

# --- actually execute instructions ---
def move(ctx, count, src, dest):
    for _ in range(count):
        ctx[dest].append(ctx[src][-1])
        ctx[src] = ctx[src][:-1]

def move2(ctx, count, src, dest):
    ctx[dest] += ctx[src][-count:]
    ctx[src] = ctx[src][:-count]

for line in f[lineCount:]:
    moveCount, src, dest = map(int, re.findall(r"\d+", line))
    move(stacks, moveCount, src-1, dest-1)
    move2(stacks2, moveCount, src-1, dest-1) # part 2

ostr = ''
for stack in stacks:
    ostr += stack[-1]
ostr += " "
for stack in stacks2:
    ostr += stack[-1]
print(ostr)
