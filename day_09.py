from helper import Day

def extrapolate(line,part_two):
    lines = [line]
    while set(lines[-1]) != {0}:
        new_line = [a - b for a, b in zip(line[1:],line[:-1])]
        lines.append(new_line) 
        line = [x for x in new_line]

    for i in range(len(lines)-2,-1,-1):
        lines[i].append(lines[i][-1]+lines[i+1][-1])
        lines[i].insert(0,lines[i][0]-lines[i+1][0])

    if part_two:
        return lines[0][0]
    
    return lines[0][-1]


def solution(data,part_two):       
    total = 0      
    for line in data:
        line = [int(i) for i in line.split()]
        total += extrapolate(line,part_two)

    return total


day = Day(9,solution)
# day.test()
day.solve()
