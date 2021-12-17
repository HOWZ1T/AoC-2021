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
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def check(lines):
    stacks = []
    for i in range(len(lines)):
        l = lines[i]
        stk = []
        valid = True
        for j in range(len(l)):
            c = l[j]
            if c in '({[<':
                stk.append(c)
            elif tag_dict[c] == stk[-1]:
                stk.pop()
            else:
                valid = False
                break
        if valid:
            stacks.append(stk)

    completion_strings = []
    for stk in stacks:
        completion_string = ''
        while len(stk) > 0:
            completion_string += tag_dict[stk.pop()]
        completion_strings.append(completion_string)
    return completion_strings


def solve(lines):
    lines = [l.strip() for l in lines if len(l.strip()) > 0]
    completions = check(lines)

    scores = []
    for completion in completions:
        total_score = 0
        for c in completion:
            total_score *= 5
            total_score += tag_points[c]
        scores.append(total_score)

    scores.sort()
    print(scores[int(len(scores)/2)])
