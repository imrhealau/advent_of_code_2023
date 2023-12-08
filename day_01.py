from helper import Day

def solution(data,part_two):

    q1_sum = 0
    for i in data:
        num_list = []
        for j in i:
            if j.isnumeric():
                num_list.append(int(j))  
        q1_sum += (num_list[0]*10 + num_list[-1])
    
    if part_two:
        num_dict = {
            'one':1,
            'two':2,
            'three':3,
            'four':4,
            'five':5,
            'six':6,
            'seven':7,
            'eight':8,
            'nine':9
        }

        q2_sum = 0

        def is_number(line, position):
            if line[position].isnumeric():
                return int(line[position])
            for a,b in num_dict.items():
                if line[position:position+len(a)] == a:
                    return int(b)   

        for line in data:
            first_num = 0
            last_num = 0
            for index in range(len(line)):
                num = is_number(line, index)
                if num is not None:
                    if first_num  == 0:
                        first_num = is_number(line, index)
                    last_num = is_number(line, index)

            q2_sum += (first_num*10 + last_num)
        
        return q2_sum
    return q1_sum

day = Day(1,solution)

day.solve()
