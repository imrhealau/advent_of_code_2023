from helper import get_day

data = get_day(4)

# data = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
# "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
# "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
# "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
# "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
# "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 1"]

sum_q1 = 0
sum_q2 = 0
card_count = {}

for line in range(1,len(data)+1):
    card_count[str(line)]=1

card = 0
for line in data:
    card += 1

    pairs = line.split(": ")[1].split("| ")
    my_num = list(filter(None,pairs[0].split(" ")))
    elf_num = list(filter(None,pairs[1].split(" ")))

    count = 0
    for i in my_num:
        if i in elf_num:
            count += 1

    if count > 0:
        points = 2**(count-1)
        sum_q1 += points

    for j in range(1,count+1):
        num = card + j
        if str(num) not in card_count:
            card_count[str(num)] = 1
        card_count[str(num)] += card_count[str(card)]

sum_q2 = sum(card_count.values())

print(sum_q1)
print(sum_q2)



            
        
