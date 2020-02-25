list = [90, 2, 4, 33, 1, 24, 103]
answer = 0;
j = 0;
i = 0;

for p in range(len(list)): 
    if j < list[p]:
        i = j
        j = list[p]
    elif i < list[p]:
        i = list[p]

answer = j + i;
print(str(j))
print(str(i))
print(str(answer));
