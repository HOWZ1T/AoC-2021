tag_dict = {
    '(': ')',
    ')': '(',
    '[': ']',
    ']': '[',
    '{': '}',
    '}': '{',
    '<': '>',
    '>': '<',
}

tag_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def check(lines):
    errors = []
    for i in range(len(lines)):
        l = lines[i]
        stk = []
        for j in range(len(l)):
            c = l[j]
            if c in '({[<':
                stk.append(c)
            elif tag_dict[c] == stk[-1]:
                stk.pop()
            else:
                # tuple (line, line_pos, char_pos, expected, actual)
                errors.append((l, i+1, j+1, tag_dict[stk[-1]], c))
                break
    return errors


def solve(lines):
    lines = [l.strip() for l in lines if len(l.strip()) > 0]
    errs = check(lines)

    points = {
        ')': 0,
        '}': 0,
        ']': 0,
        '>': 0
    }
    for _, i, j, e, a in errs:
        print(f"error at line: {i}, pos: {j}, expected: '{e}', got: '{a}'")
        points[a] += 1

    for k, v in points.items():
        points[k] = tag_points[k] * v

    score = sum([v for v in points.values()])
    print(f"syntax error score: {score}")

