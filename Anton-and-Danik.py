num_games = int(input())

outcomes = input().strip()

anton_wins = 0
danik_wins = 0

for result in outcomes:
    if result == 'A':
        anton_wins += 1  
    else:
        danik_wins += 1 

if anton_wins > danik_wins:
    print("Anton")
elif danik_wins > anton_wins:
    print("Danik")
else:
    print("Friendship")
