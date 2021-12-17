digit_seg = {
    1: ('cf', 2),  # unique comb
    4: ('bcdf', 4),  # unique comb
    7: ('acf', 3),  # unique comb
    8: ('abcdefg', 7),  # unique comb

    2: ('acdeg', 5),
    3: ('acdfg', 5),
    5: ('abdfg', 5),
    6: ('abdefg', 6),
    9: ('abcdfg', 6),
    0: ('abcefg', 6),
}


def solve(lines):
    # list of digits, 4 seg display pairs
    lines = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']
    displays = [l.strip().split(' | ') for l in lines if len(l.strip()) > 0]

    digit_map = {}
    for raw_digits, raw_segs in displays:
        digits = raw_digits.split(' ')
        for digit in digits:
            match len(digit):
                case 2:
                    digit_map[1] = digit
                case 4:
                    digit_map[4] = digit
                case 3:
                    digit_map[7] = digit
                case 7:
                    digit_map[8] = digit

    wire_pos = {x: [] for x in 'abcdefg'}
    print(wire_pos)
    #    0000
    #   1    2
    #   1    2
    #    3333
    #   4    5
    #   4    5
    #    6666
    for num, digit in digit_map.items():
        match num:
            case 1:
                for d in digit:
                    wire_pos[d].extend([2, 5])
            case 4:
                for d in digit:
                    wire_pos[d].extend([0, 2, 5])
            case 7:
                for d in digit:
                    wire_pos[d].extend([1, 2, 3, 5])

            case 8:
                for d in digit:
                    wire_pos[d].extend([0, 1, 2, 3, 4, 5, 6])
    for k, v in wire_pos.items():
        print(f"{k} : {v}")
    # TODO