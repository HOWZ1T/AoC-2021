from itertools import chain


def create_map(point_pairs):
    mp = [[0 for _ in range(1000)] for _ in range(1000)]

    for point_a, point_b in point_pairs:
        # get left and right points
        if point_a[0] <= point_b[0]:
            left = point_a
            right = point_b
        else:
            left = point_b
            right = point_a

        # get direction of line movement
        y_diff_inv = -1 * (left[1] - right[1])
        x_diff_inv = -1 * (left[0] - right[0])

        # traverse line marking points it touches
        while left != right:
            mp[left[1]][left[0]] += 1
            if x_diff_inv > 0:
                left[0] += 1
            elif x_diff_inv < 0:
                left[0] -= 1

            if y_diff_inv > 0:
                left[1] += 1
            elif y_diff_inv < 0:
                left[1] -= 1
        mp[left[1]][left[0]] += 1
    return mp


def solve(lines):
    point_pairs = [[list(map(int, coord.strip().split(','))) for coord in l.split('->')] for l in lines]
    dangerous_points_count = len([x for x in list(chain.from_iterable(create_map(point_pairs))) if x >= 2])
    print(dangerous_points_count)
