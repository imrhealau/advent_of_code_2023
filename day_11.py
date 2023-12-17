from helper import Day

def expand_galaxy(data):
    new_rows=[]
    galaxy_y=[]
    new_data=[]
    col_dict={}

    for num, row in enumerate(data):
        if '#' not in row:
            new_rows.append(row)
            galaxy_y.append(2)
        else:
            galaxy_y.append(1)
        new_rows.append(row)

    for row in new_rows:
        for i in range(len(row)):
            col_dict[i] = 2
        
    for row in new_rows:
        for idx, ele in enumerate(row):
                if ele == '#':
                    col_dict[idx] = 1

    for rows in new_rows:
        string = ''
        for col,ele in zip(list(col_dict.values()),rows):
            if col == 2:
                string += ele
            string += ele
        new_data.append(string)
    
    galaxy_x=list(col_dict.values())

    return new_data,galaxy_x,galaxy_y

def find_dist(data):
    count = 0
    galaxy_dict = {}
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == '#':
                count += 1
                galaxy_dict[count] = (row,col)

    dist_sum = 0
    items = list(galaxy_dict.items())
    for ind, (k1, v1) in enumerate(items):
        for k2, v2 in items[ind+1:]:
            y_delta = max(v1[0], v2[0]) - min(v1[0], v2[0])
            x_delta = max(v1[1], v2[1]) - min(v1[1], v2[1])
            dist_sum += y_delta + x_delta

    return dist_sum

def find_dist2(data,galaxy_x,galaxy_y,fac=10):
    count = 0
    galaxy_dict = {}
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == '#':
                count += 1
                galaxy_dict[count] = (row,col)

    dist_sum = 0
    items = list(galaxy_dict.items())
    for ind, (k1, v1) in enumerate(items):
        for k2, v2 in items[ind+1:]:
            y_weight = galaxy_y[min(v1[0], v2[0]):max(v1[0], v2[0])].count(2)
            x_weight = galaxy_x[min(v1[1], v2[1]):max(v1[1], v2[1])].count(2)
            y_delta = max(v1[0], v2[0]) - min(v1[0], v2[0]) - y_weight
            x_delta = max(v1[1], v2[1]) - min(v1[1], v2[1]) - x_weight
            dist_sum += y_delta + x_delta + fac * y_weight + fac * x_weight
            # print(v1,v2,y_weight,x_weight,dist_sum)
            # break
    return dist_sum
        


def solution(data,part_two):  
    data_new,galaxy_x,galaxy_y = expand_galaxy(data)

    if part_two:
        return find_dist2(data,galaxy_x,galaxy_y,1e6)

    return find_dist(data)




day = Day(11,solution)
# day.test() 
day.solve()