def solve(lines):
    positions = list(map(int, lines[0].split(',')))
    n = len(positions)
    positions.sort()
    q_size = int(round(n / 4))
    q1 = positions[q_size]
    q3 = positions[n-q_size-1] if n % 2 == 0 else positions[n-q_size]

    # tuple of target point and total fuel cost
    solutions = []
    for i in range(q1, q3+1):
        # calculate fuel costs
        # n is absolute diff between current and target pos
        # fuel = (n * (n+1)) / 2
        fuel = sum([(x * (x + 1))/2 for x in [abs(p-i) for p in positions if p != i]])
        solutions.append((i, fuel))
    optimal_solution = min(solutions, key=lambda x: x[1])
    print(optimal_solution)
