from helper import get_day

data = get_day(3)

# data = ['467..114..',
# '...*......',
# '..35..633.',
# '......#...',
# '617*......',
# '.....+.58.',
# '..592.....',
# '......755.',
# '..*$.*....',
# '.664.598..']

special_char = "!@#$%^&*()-+?_=,<>/"

def check_char(data,y,x):
    for y_diff in [-1,0,1]:
        for x_diff in [-1,0,1]:
            new_y = y + y_diff
            new_x = x + x_diff
            if new_x < 0 or new_y < 0 or \
               new_x >= len(data[0]) or new_y >= len(data):
                continue
            if data[new_y][new_x] in special_char:
                return True
    return False

count = 0
start_pos = []
end_pos = []
for y, line in enumerate(data):
    for x, unit in enumerate(line):
        if (x == 0 and unit.isdigit()) or ((x != 0 and not line[x-1].isdigit()) and unit.isdigit()):
            start_pos.append((y,x))
        if (x == len(line)-1 and unit.isdigit()) or ((x != len(line)-1 and not line[x+1].isdigit()) and unit.isdigit()):
            end_pos.append((y,x))

sum_q1 = 0
for (y1,x1),(y2,x2) in zip(start_pos,end_pos):
    for x in range(x1,x2+1):
        status = check_char(data,y1,x)
        if status:
            sum_q1 += int(data[y1][x1:x2+1])
            break

# print(sum_q1)

#------------
# Part 2
#------------

def find_star(data):
    star_coor = []
    for y, line in enumerate(data):
        for x, unit in enumerate(line):
            if data[y][x] == '*':
                star_coor.append([y,x])
    return star_coor

def check_star(data,star_coor,y,x):
    for y_diff in [-1,0,1]:
        for x_diff in [-1,0,1]:
            new_y = y + y_diff
            new_x = x + x_diff
            if new_x < 0 or new_y < 0 or \
               new_x >= len(data[0]) or new_y >= len(data):
                continue
            if [new_y,new_x] == star_coor:
                return True
    return False        

star_coor = find_star(data)
sum_q2 = 0
for coor in star_coor:
    num_coor = []
    star_num = []
    for (y1,x1),(y2,x2) in zip(start_pos,end_pos):
        for x in range(x1,x2+1):
            status = check_star(data,coor,y1,x)
            if status:
                num_coor.append((y1,x1,x2))
    num_coor = list(dict.fromkeys(num_coor))
    # print(num_coor)
    for num in num_coor:
        star_num.append(data[num[0]][num[1]:num[2]+1])
    # print(star_num)
    
    if len(star_num) == 2:
        print(star_num)
        sum_q2 += int(star_num[0]) * int(star_num[1])

print(sum_q2)

