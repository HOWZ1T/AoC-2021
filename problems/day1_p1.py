def solve():
    numbers = []

    # read in numbers from file
    with open('inputs/d1p1.txt', 'r') as f:
        for line in f.readlines():
            if len(line) == 0:
                continue
            numbers.append(int(line.strip()))

    increased = 0
    for i in range(1, len(numbers)):
        prev = numbers[i-1]
        cur = numbers[i]
        if cur > prev:
            increased += 1

    print(increased)
