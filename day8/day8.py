forest = [[int(i)for i in line.strip('\n')] for line in open("day8.input").readlines()]
width = len(forest[0])
height = len(forest)
visible = []
for i in forest:
    for j in i:
        visible.append(0)

sides = [(0,0,1,0,), (0,0,0,1), 
        (width-1, height-1, -1, 0), (width-1, height-1, 0, -1)]

for scan in sides:
    x,y, x_incr, y_incr = scan
    x_side, y_side = 0, 0
    x_side_incr = y_incr
    y_side_incr = x_incr
    last_highest = -1
    while(x + x_side * x_side_incr >= 0 and x + x_side * x_side_incr < width ) and (y + y_side * y_side_incr >= 0 and y + y_side * y_side_incr < height):
        this_scan = 0
        while (x >= 0 and x < width) and (y >= 0 and y < height):
            i_x = x + x_side * x_side_incr
            i_y = y + y_side * y_side_incr
            tree = forest[i_y][i_x]
            if tree > last_highest:
                visible[i_y * width + i_x] = 1
                last_highest = tree
                this_scan += 1
            x += x_incr
            y += y_incr
        x_side += 1 
        y_side += 1 
        x = scan[0]
        y = scan[1]
        last_highest = -1

# part 2
directions = [(0,1), (1,0), (-1, 0), (0,-1)]
best_score = -1
for x_base in range(0, width):
    for y_base in range(0, height):
        treeHeight = forest[y_base][x_base]
        view_score = 1
        if (x_base == 0) or (y_base == 0) or (x_base == width - 1) or (y_base == height - 1):
            continue
        for scan in directions:
            view_dist = 0
            x = x_base
            y = y_base
            while (x < width and x >= 0) and (y < height and y >= 0):
                if ((forest[y][x] < treeHeight) or (x == x_base and y == y_base)):
                    view_dist += 1
                    x += scan[0]
                    y += scan[1]
                    if x == 0 or y ==0 or x == width - 1 or y == height - 1:
                        break
                else:
                    break
            view_score *= view_dist
        if view_score > best_score:
            best_score = view_score

print(sum(visible))
print("part2", best_score)
