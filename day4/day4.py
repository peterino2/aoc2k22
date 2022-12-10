file_contents = __import__('re').findall(r"(\d+)-(\d+),(\d+)-(\d+)", open('day4.input').read())
calc_results = lambda a, b, x, y: [(a <= x and b >= y) or (x <= a and y >= b), a <= y and x <= b]
sets = [calc_results(*[ int(i) for i in l]) for l in file_contents]
print(f"part1={sum(s[0] for s in sets)} part2={sum(s[1] for s in sets)}")


import re
part1 = 0
part2 = 0

for line in open('day4.input').readlines():
    a, b, x, y = map(int, line.split('-'))
    part1 += 1 if (a <= x and b >= y) or (x <= a and y >= b) else 0
    part2 += 1 if a <= y and x <= b else 0

print(f"part1={part1} part2={part2}")