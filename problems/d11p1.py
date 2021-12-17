import copy


def pg(pgrid, grid):
    for i in range(len(grid)):
        prow = ' '.join(map(str, pgrid[i]))
        row = ' '.join(map(str, grid[i]))
        print("%s\t--->\t  %s" % (prow, row))
    print('\n\n')


def simulate(grid, steps, flashes=0):
    if steps == 0:
        return flashes

    # add energy
    grid = [[col+1 for col in row] for row in grid]
    flashed = []

    # simulate flashes
    prev_grid = []
    while prev_grid != grid:
        prev_grid = copy.deepcopy(grid)
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                v = grid[y][x]
                if v > 9 and (x, y) not in flashed:
                    flashed.append((x, y))
                    flashes += 1
                    v = 0

                    # add energy to neighbours
                    for y1 in range(y-1, y+2):
                        for x1 in range(x-1, x+2):
                            grid[y][x] += 1
                pg(prev_grid, grid)
                grid[y][x] = v

    return simulate(grid, steps-1, flashes)


def solve(lines):
    lines = [[int(c) for c in l.strip()] for l in lines if len(l.strip()) > 0]
    print(simulate(lines, 1))
