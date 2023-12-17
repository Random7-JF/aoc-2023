data = open("/home/random/projects/aoc-2023/day6/day6.input")
lines = data.read().splitlines()

nums = []
for line in lines:
    num = ""
    for char in line:
        if char.isnumeric():
            num = num + char
    nums.append(num)

print(f"numbers: {nums}")
time = int(nums[0])
distance = int(nums[1])
print(f"times: {time} distance: {distance}")

winners = dict()
hold = 0
wins = 0
losses = 0
while hold < time:
    dur = distance - hold
    total = dur * hold
    print(f"hold: {hold} dur:{dur} total:{total}")
    if distance < total:
        wins += 1
    else:
        losses += 1
    hold += 1
winners["race"] = wins
print(f"winners: {winners}")
print(f"Lost: {losses}")
print(f"times: {time} distance: {distance}")
