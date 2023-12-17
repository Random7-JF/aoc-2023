data = open("/home/random/projects/aoc-2023/day6/day6.input")
lines = data.read().splitlines()

times = []
distance = []
nums = []
for line in lines:
    line_split = line.split(":")
    x = line_split[1].split(" ")
    num = ""
    for i, y in enumerate(x):
        print(f"y: {y}")
        if i >= len(x) - 1:
            print("last num found")
        if y != "":
            nums.append(y)

times = nums[0:4]
distance = nums[4:8]
print(f"times: {times} distance: {distance}")

winners = dict()
for index, race in enumerate(times):
    hold = 0
    wins = 0
    while hold <= int(race):
        hold = hold
        dur = int(race) - hold
        total = dur * hold
        print(f"hold: {hold} dur:{dur} total:{total}")
        if total > int(distance[index]):
            wins += 1
        hold += 1
    winners[int(race)] = wins

print(f"winners: {winners}")

answer = 1
for item in winners:
    answer = answer*winners[item]
print(f"Answer: {answer}")