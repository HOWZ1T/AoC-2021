def solve():
    numbers = []

    # read in numbers from file
    with open('inputs/d1p1.txt', 'r') as f:
        for line in f.readlines():
            if len(line) == 0:
                continue
            numbers.append(int(line.strip()))

    sliding_sums = []
    window_size = 3
    for i in range(len(numbers)-window_size+1):
        sliding_sums.append(sum(numbers[i:i+window_size]))

    increased = 0
    for i in range(1, len(sliding_sums)):
        prev = sliding_sums[i-1]
        cur = sliding_sums[i]
        if cur > prev:
            increased += 1

    print(increased)