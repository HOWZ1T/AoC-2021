def solve(lines):
    print(sum([sum([1 for seg in segs.split(' ') if len(seg) in [2, 3, 4, 7]]) for _, segs in [l.strip().split(' | ') for l in lines if len(l.strip()) > 0]]))