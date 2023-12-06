from helper import get_day, get_test_data

data = get_day(6)

# data = get_test_data()

#------------
# Part 1
#------------

time_list = data[0].split()[1:]
dist_list = data[1].split()[1:]

# distance = speed * time
count_product = 1
for i in range(len(time_list)):
    count = 0
    for v in range(int(time_list[i])):
        d = v * (int(time_list[i]) - v)
        if d > int(dist_list[i]):
            count += 1
    count_product *= count

# print(count_product)

#------------
# Part 2
#------------
time_list_2 = ''.join(time_list)
dist_list_2 = ''.join(dist_list)

count = 0
for v in range(int(time_list_2)):
    d = v * (int(time_list_2) - v)
    if d > int(dist_list_2):
        count += 1

# print(count)
