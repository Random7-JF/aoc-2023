data = open("/home/random/projects/aoc-2023/day6/day6-test.input") 
lines = data.read().splitlines()

times = []
distance = []
nums = []
for line in lines:
    l = line.split(":")
    x = l[1].split(" ")
    num = ""
    for i, y in enumerate(x):
        print(f"y: {y}")
        if i >= len(x) - 1:
            print(f"last num found")
        if y != "":
            nums.append(y)

times = nums[0:3]
distance = nums[3:6]
print(f"times: {times} distance: {distance}") 


