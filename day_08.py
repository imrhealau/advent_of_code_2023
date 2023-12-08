from helper import Day
from math import lcm, gcd

def solution(data,part_two):
    instruction = data[0]
    #---------
    # Part 1  
    #--------- 
    network = {}
    for line in data[2:]:
        network[line.split(' = ')[0]] = line.split(' = ')[1]
    count = 0
    location = 'AAA'
    while True:
        if instruction[count%len(instruction)] == 'L':
            location = network[location][1:4]
        elif instruction[count%len(instruction)] == 'R':
            location = network[location][6:9]
        if location == 'ZZZ':
            break
        count += 1

    #---------
    # Part 2   
    #--------- 
    if part_two:
        start_pos = {}
        end_pos = {}
        for i in range(len(data[2:])):
            if list(network.keys())[i][2] == 'A':
                start_pos[list(network.keys())[i]]=1

        for pos in list(start_pos.keys()):
            count = 0
            location = pos
            while True:
                # if location[2] == 'X':
                #     print('break')
                #     break
                if instruction[count%len(instruction)] == 'L':
                    location = network[location][1:4]
                elif instruction[count%len(instruction)] == 'R':
                    location = network[location][6:9]
                if location[2] == 'Z':
                    end_pos[location]= count + 1
                    break
                count += 1
            start_pos[pos] = count + 1

        for pos in list(end_pos.keys()):
            original_count = end_pos[pos] 
            count = end_pos[pos]
            location = pos
            while True:
                # if location[2] == 'X':
                #     break
                if instruction[count%len(instruction)] == 'L':
                    location = network[location][1:4]
                elif instruction[count%len(instruction)] == 'R':
                    location = network[location][6:9]
                # print(location)
                if location == pos:
                    break
                count += 1
            end_pos[pos] = count + 1 - original_count
    
        lcm = 1
        for i in list(end_pos.values()):
            lcm = lcm*i//gcd(lcm, i)

        return lcm
    return count + 1


day = Day(8,solution)
day.solve()

