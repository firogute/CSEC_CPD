calories = list(map(int, input().split()))
sequence = input()
total_calories = 0

for char in sequence:
    index = int(char) - 1
    total_calories += calories[index]

print(total_calories)
