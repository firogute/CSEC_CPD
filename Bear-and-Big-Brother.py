small, big = map(int, input().split())

count = 0
while small <= big:
    small *= 3
    big *= 2
    count += 1

print(count)
