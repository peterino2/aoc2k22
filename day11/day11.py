import re

f = [ line.strip('\n') for line in open("day11.input").readlines()]

new = None
old = None

def simulate(isPart2):

    def do_testOp(param, opstr):
        global old
        global new
        old = param
        opstr = "global new\nglobal param\n" + opstr
        exec(opstr) # Lmao 
        return new

    monkeys = []

    lineid = 0
    while lineid < len(f):
        line = f[lineid]
        if line.startswith("Monkey"):
            si, op, test, trueOp, falseOp = f[lineid+1:lineid+6]
            monkey = []
            monkey.append([int(x) for x in si.split(":")[1].split(',')])
            monkey.append(op.split(":")[1].strip())
            monkey.append(int(re.findall('(\d+)', test)[0]))
            monkey.append(int(re.findall('(\d+)', trueOp)[0]))
            monkey.append(int(re.findall('(\d+)', falseOp)[0]))
            monkeys.append(monkey)
            lineid += 5
        else:
            lineid += 1

    lcm = 1
    for monkey in monkeys:
        lcm *= monkey[2]

    inspections = [0 for i in range(len(monkeys))]
    for i in range(10000 if isPart2 else 20):
        for k, monkey in enumerate(monkeys):
            while len(monkey[0]) > 0:
                item = monkey[0][0]
                monkey[0] = monkey[0][1:]
                new_worry = do_testOp(item, monkey[1])
                inspections[k] += 1
                if not isPart2:
                    new_worry = new_worry // 3
                if new_worry % monkey[2] == 0:
                    if isPart2:
                        new_worry = new_worry % lcm
                    monkeys[monkey[3]][0].append(new_worry)
                else:
                    if isPart2:
                        new_worry = new_worry % lcm
                    monkeys[monkey[4]][0].append(new_worry)

    inspections.sort()
    print("worry levels: ", "(part2) " if isPart2 else "", inspections[-1] * inspections[-2], inspections)

simulate(isPart2=False)
simulate(isPart2=True)