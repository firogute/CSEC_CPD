res_array = []
for i in range(5):
    res_array.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        if res_array[i][j] == 1:
            totalMove = abs(i-2) + abs(j-2)
            print(totalMove)
            break
