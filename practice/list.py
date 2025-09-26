a = [1, 19, 21, 24]

missing = [x for x in range(min(a), max(a))if x not in a]
print("Missing numbers:", missing)
print("Count of missing numbers:", len(missing))
