## PART 1 ##

fname = "day6\data\\data-day6.txt"
f = open(fname)

fish_list = f.read().split(',')
fish_list = list(map(int, fish_list))

for i in range(1,257):
    j=0
    for j in range(0, len(fish_list)):
        if fish_list[j] == 0:
            fish_list.append(8)
            fish_list[j] = 7
        fish_list[j] -= 1

print(len(fish_list))