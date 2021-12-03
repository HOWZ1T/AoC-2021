from typing import List


def cb(nums: List[str], n: int = 0, fn=max) -> str:
    """
    Gets the Common Bit (cb) at position n from a list of bit strings using the given function.

    :param nums: list of bit strings
    :param n: the index to get the common bit from
    :param fn: the min/max function to determine common bit
    :return: the common bit as string
    """
    x = []
    for num in nums:
        x.append(num[n])
    d = {y: x.count(y) for y in x}
    if d['0'] == d['1']:
        return '1' if fn == max else '0'
    return fn(d, key=d.get)


def get_rating(nums: List[str], fn=max) -> int:
    i = 0
    while len(nums) > 1:
        b = cb(nums, i, fn)
        nums = [n for n in nums if n[i] == b]
        i += 1
    return int(nums[0], base=2)


def solve(lines):
    nums = [l.strip() for l in lines if len(l.strip()) > 0]
    print(get_rating(nums) * get_rating(nums, min))
