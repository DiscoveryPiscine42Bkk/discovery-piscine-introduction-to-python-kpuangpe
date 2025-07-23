original = [2, 8, 9, 48, 8, 22, -12, 2]
unique = [x for x in original if original.count(x) == 1]
transformed = [x + 1 for x in unique]
print(original)
print(transformed)