import collections


def solve(s, times=1, num_mult=1):
    class Wrapper:
        def __init__(self, n):
            self.n = n

    nums = collections.deque(map(Wrapper, map(int, s.split())))
    order = list(nums)

    # Multiplier for part 2
    for n in nums:
        n.n *= num_mult

    for _ in range(times):
        for n in order:
            idx = nums.index(n)
            nums.rotate(-idx)
            nums.popleft()
            nums.rotate(-n.n)
            nums.insert(0, n)

    nums = [n.n for n in nums]

    zero_idx = nums.index(0)

    return sum(nums[(zero_idx + off) % len(nums)] for off in (1000, 2000, 3000))


def part1(s):
    answer = solve(s)


def part2(s):
    answer = solve(s, 10, num_mult=811589153)


input = open("2022/data/20.txt").read()
part1(input)
part2(input)
