def solve(lines):
    positions = list(map(int, lines[0].split(',')))
    n = len(positions)
    positions.sort()

    if n % 2 == 0:
        mid = int(n / 2)
        q2 = (positions[mid] + positions[mid-1])/2
    else:
        mid = int(((n + 1) / 2) - 1)
        q2 = positions[mid]

    fuel = sum([abs(p-q2) for p in positions if p != q2])
    print(fuel)