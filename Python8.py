coordinates = [(2, 4), (1, 3), (6, 8), (7, 2), (0, 0)]
result = []
for x, y in coordinates:
    if x % 2 == 0 and y % 2 == 0:
        result.append((x, y))

print("Output:", result)
