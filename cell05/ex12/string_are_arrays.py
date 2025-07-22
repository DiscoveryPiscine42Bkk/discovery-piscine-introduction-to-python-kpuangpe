import sys
if len(sys.argv) != 2:
    print("none")
else:
    s = sys.argv[1]
    result = ""
    for char in s:
        if char == 'z':
            result += 'z'
    print(result if result else "none")