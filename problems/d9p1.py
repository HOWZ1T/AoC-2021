from itertools import chain


def get_neighbours(x, y, grid):
    neighbours = []
    if x-1 >= 0:
        neighbours.append(grid[y][x-1])
    if x+1 < len(grid[y]):
        neighbours.append(grid[y][x+1])
    if y-1 >= 0:
        neighbours.append(grid[y-1][x])
    if y+1 < len(grid):
        neighbours.append(grid[y+1][x])
    return neighbours


def solve(lines):
    grid = [[int(c) for c in line.strip()] for line in lines if len(line.strip()) > 0]
    print(sum(list(map(lambda x: x+1, list(chain.from_iterable([[grid[y][x] for x in range(len(grid[y])) if grid[y][x] < min(get_neighbours(x, y, grid))] for y in range(len(grid))]))))))
