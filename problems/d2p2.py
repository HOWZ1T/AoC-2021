def solve(lines):
    # read in commands
    commands = []
    for line in lines:
        if len(line) == 0:
            continue
        cmd, val = tuple(line.split(' '))
        cmd = cmd.strip().lower()
        val = int(val)
        commands.append((cmd, val))

    pos_x = 0
    depth = 0
    aim = 0

    for cmd, val in commands:
        match cmd:
            case 'forward':
                pos_x += val
                depth += aim * val
            case 'up':
                aim -= val
            case 'down':
                aim += val
            case _:
                print(f"unknown command: {cmd}")

    print(pos_x * depth)
