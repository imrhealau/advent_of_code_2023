from helper import get_day

data = get_day(1)

q1_sum = 0
for i in data:
    num_list = []
    for j in i:
        if j.isnumeric():
            num_list.append(int(j))  
    q1_sum += (num_list[0]*10 + num_list[-1])

print(q1_sum)

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
        
print(q2_sum)

# f = lambda str, dir: min((str[::dir].find(num[::dir])%99, i) for i, num in enumerate(
#     '1 2 3 4 5 6 7 8 9 one two three four five six seven eight nine'.split()))[1]%9+1

# print(sum(10*f(x, 1) + f(x, -1) for x in data))