n = int(input())

ans = 0

for _ in range(n):
    lst = list(map(int, input().rstrip().split()))
    total = sum(lst)

    if total >= 2:
        ans += 1

print(ans)
