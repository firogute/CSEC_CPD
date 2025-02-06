s = input()
total_rotations = 0
current_pos = ord('a')

for char in s:
    target_pos = ord(char)
    clockwise = abs(target_pos - current_pos)
    counterclockwise = 26 - clockwise
    total_rotations += min(clockwise, counterclockwise)
    current_pos = target_pos

print(total_rotations)
