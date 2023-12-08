from helper import Day
import re
import math
from functools import reduce

def solution(data,part_two):
    instructions = data[0].strip()
    nodes = {m[0]: tuple(m[1:]) for m in (re.findall("\w+", l) for l in data[2:])}

    def num_steps(pos, end_pred):
        steps = 0

        while True:
            for inst in instructions:
                steps += 1
                pos = nodes[pos][0 if inst == 'L' else 1]
                if end_pred(pos):
                    return steps

        return steps

    def lcm(a, b):
        return a * b // math.gcd(a, b)

    
    if part_two:
        return print("2:", reduce(lcm, (num_steps(p, lambda p: p.endswith('Z')) for p in nodes.keys() if p.endswith('A'))))
    return print("1:", num_steps('AAA', lambda p: p == 'ZZZ'))

day = Day(8,solution)
day.solve()
