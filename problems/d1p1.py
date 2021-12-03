def solve(lines):
    numbers = []

    for line in lines:
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
