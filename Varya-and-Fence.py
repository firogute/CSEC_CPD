num_friends, fence_height = map(int, input().split())

friends_heights = list(map(int, input().split()))

total_width = 0

for height in friends_heights:

    if height > fence_height:
        total_width += 2
    else:
        total_width += 1


print(total_width)
