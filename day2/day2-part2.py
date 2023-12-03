RED = 12
GREEN = 13
BLUE = 14
data = open("day2.input")
lines = data.readlines()
invalidMatches = []
powers = []
for line in enumerate(lines, 1):
    games = line[1].strip().replace("\n","").split(";")
    minRed, minGreen, minBlue = 1,1,1
    for match in games:
        currentRedCount, currentGreenCount, currentBlueCount = 0,0,0
        m = match.replace(f"Game {line[0]}:", "").strip().split(", ")
        #m - ['1 red', '2 green', '6 blue']
        for colour in m:
            num = colour[0:2]
            if "red" in colour:
                currentRedCount = int(num)
                if currentRedCount > minRed:
                    minRed = currentRedCount
            elif "green" in colour:
                currentGreenCount = int(num)
                if currentGreenCount > minGreen:
                    minGreen = currentGreenCount
            elif "blue" in  colour:
                currentBlueCount = int(num)
                if currentBlueCount > minBlue:
                    minBlue = currentBlueCount
            if currentRedCount > RED or currentBlueCount > BLUE or currentGreenCount > GREEN:
                if line[0] not in invalidMatches:
                    invalidMatches.append(line[0])
    powers.append((line[0], minRed*minGreen*minBlue))
sum = 0
for match in enumerate(lines, start=1):
    if match[0] not in invalidMatches:
        sum += match[0]
powersum = 0
for power in powers:
    powersum += power[1]
print(f"Total Sum: {sum}")
print(f"Total Power: {powersum}")
