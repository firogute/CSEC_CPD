string = input()
capital = sum(1 for c in string if c.isupper())
small = sum(map(str.islower, string))

if small > capital or capital == small:
    print(string.lower())
else:
    print(string.upper())
