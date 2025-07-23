import sys
if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    count = text.split().count(keyword)
    if fount == 0:
        print("none")
    else:
        print(count)