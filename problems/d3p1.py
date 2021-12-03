def solve(lines):
    lines = [l.strip() for l in lines if len(l.strip()) > 0]
    rows = [[int(x) for x in line] for line in lines]
    cols = [list(col) for col in zip(*rows)]
    gamma = int(''.join([str(max(set(col), key=col.count)) for col in cols]), base=2)
    epsilon = int(''.join([str(min(set(col), key=col.count)) for col in cols]), base=2)
    print(gamma * epsilon)
