from dataclasses import dataclass


@dataclass
class Spawn:
    period: int = 0
    num_fish: int = 0


def simulate(fishes, n):
    total = n
    freq = {}
    for fish in fishes:
        freq[fish] = fishes.count(fish)

    spawn_periods = [Spawn(k, v) for k, v in freq.items()]
    while n > 0:
        new_fish = 0
        for i in range(len(spawn_periods)):
            spawn = spawn_periods[i]
            if spawn.period == 0:
                spawn.period = 6
                new_fish += spawn.num_fish
            else:
                spawn.period -= 1
            spawn_periods[i] = spawn
        spawn_periods.append(Spawn(8, new_fish))
        n -= 1
        print(f"\rIteration: {total-n}", end="", flush=True)
    print("\n")
    count = 0
    for spawn in spawn_periods:
        count += spawn.num_fish
    return count


def solve(lines):
    fishes = list(map(int, lines[0].split(',')))
    print(simulate(fishes, 256))
