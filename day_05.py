from helper import get_day, get_test_data

data = get_day(5)

# data = get_test_data()

data = "\n".join([x if len(data) > 0 else "XxX" for x in data]).split("XxX")

lines = data[0].split('\n\n')
seeds = lines[0].split(": ")[1].split(" ")

map_dict = {}

for line in lines[1:]:
    line = line.split('\n')
    map_dict[line[0][:-4]] = [[int(j) for j in i.split()] for i in line[1:]]


def map_number(number, element_lists):
    for element_list in element_lists:
        if number >= element_list[1] and number < (element_list[1] + element_list[2]):
            return number + element_list[0] - element_list[1] 
    return number

def find_min_loc(seeds,map_dict):
    loc = []
    for seed in seeds:
        number = int(seed)
        for _, element_lists in map_dict.items():
            number = map_number(number, element_lists)
        loc.append(number)
    return min(loc)

print(find_min_loc(seeds,map_dict))

