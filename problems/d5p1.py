from itertools import chain


def create_map(point_pairs):
    mp = [[0 for _ in range(1000)] for _ in range(1000)]
    vertical_lines = [pp for pp in point_pairs if pp[0][0] == pp[1][0]]
    horizontal_lines = [pp for pp in point_pairs if pp[0][1] == pp[1][1]]

    for point_a, point_b in horizontal_lines:
        assert point_a[1] == point_b[1]
        y = point_a[1]
        start_x = min(point_a[0], point_b[0])
        end_x = max(point_a[0], point_b[0])
        for x in range(start_x, end_x+1):
            mp[y][x] += 1

    for point_a, point_b in vertical_lines:
        assert point_a[0] == point_b[0]
        x = point_a[0]
        start_y = min(point_a[1], point_b[1])
        end_y = max(point_a[1], point_b[1])
        for y in range(start_y, end_y+1):
            mp[y][x] += 1

    return mp


def solve(lines):
    point_pairs = [[tuple(map(int, coord.strip().split(','))) for coord in l.split('->')] for l in lines]

    # filter out diagonal lines
    point_pairs = [pp for pp in point_pairs if pp[0][0] == pp[1][0] or pp[0][1] == pp[1][1]]
    dangerous_points_count = len([x for x in list(chain.from_iterable(create_map(point_pairs))) if x >= 2])
    print(dangerous_points_count)
