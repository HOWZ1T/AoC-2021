def simulate(fishes, n):
    total = n
    while n > 0:
        new_fish = 0
        for i in range(len(fishes)):
            fish = fishes[i]
            if fish == 0:
                fish = 6
                new_fish += 1
            else:
                fish -= 1
            fishes[i] = fish
        fishes.extend([8] * new_fish)
        n -= 1
        print(f"\rIteration: {total-n}", end="", flush=True)
    print("\n")
    return fishes


def solve(lines):
    fishes = list(map(int, lines[0].split(',')))
    print(len(simulate(fishes, 256)))
