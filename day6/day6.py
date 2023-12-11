data = open("/home/random/projects/aoc-2023/day6/day6-test.input")
lines = data.read().splitlines()

## Time - Distance
races = dict()
for index, line in enumerate(lines, start=1):
    s = line.strip().split(":")
    print(f"{s[1].strip()}")
    x = s[1].strip().split(" ")
