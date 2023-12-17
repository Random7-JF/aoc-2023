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
race_duration = int(nums[0])
race_record = int(nums[1])
print(f"race_duration: {race_duration} - race_record: {race_record}")

wins = 0
speed = 0
while speed < race_duration:
    time = race_duration - speed
    result = speed * time
    speed += 1
    if result > race_record:
        wins += 1

print(f"Wins: {wins}")
