list = [1,2,3,3,3,3,3,3,3,5,6]

i=0

while i < len(list):
    if list[i] == 3:
        list.remove(list[i])
        i -= 1
        continue
    i+=1


print(list)