from itertools import chain
from functools import reduce
from rich import print


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


def calculate_basins(low_points, grid):
    basins = []
    for x, y in low_points:
        nodes = [(x, y)]
        basin_coords = []
        while len(nodes) > 0:
            cur = nodes.pop()
            cx = cur[0]
            cy = cur[1]
            basin_coords.append((cx, cy))
            cur_v = grid[cy][cx]
            neighbours = []
            if cy-1 >= 0:
                neighbours.append((cx, cy-1))
            if cy+1 < len(grid):
                neighbours.append((cx, cy+1))
            if cx-1 >= 0:
                neighbours.append((cx-1, cy))
            if cx+1 < len(grid[cy]):
                neighbours.append((cx+1, cy))

            for nx, ny in neighbours:
                if (nx, ny) in basin_coords:
                    continue
                if abs(cur_v - grid[ny][nx]) == 1 and grid[ny][nx] != 9:
                    nodes.append((nx, ny))
        basins.append(len(set(basin_coords)))
    return basins


def solve(lines):
    grid = [[int(c) for c in line.strip()] for line in lines if len(line.strip()) > 0]
    low_points_coords = list(chain.from_iterable([
        [(x, y) for x in range(len(grid[y])) if grid[y][x] < min(get_neighbours(x, y, grid))]
        for y in range(len(grid))
    ]))

    basins = calculate_basins(low_points_coords, grid)
    basins.sort()
    print(reduce(lambda x, y: x * y, basins[-3:]))