RED = 12
GREEN = 13
BLUE = 14
data = open("day2.input")
lines = data.readlines()
invalidGames = []
for line in enumerate(lines, 1):
    games = line[1].strip().replace("\n","").split(";")
    for game in games:
        currentRedCount = 0
        currentGreenCount = 0
        currentBlueCount = 0
        #x = game.replace(f'Game {line[0]}:', '')
        for y in enumerate(game):
            if y[1].isnumeric():
                if game[y[0]+1].isnumeric():
                    if game[y[0]+3] == "b":
                        currentBlueCount = int(f"{y[1]}{game[y[0]+1]}")
                    elif game[y[0]+3] == "r":
                        currentRedCount = int(f"{y[1]}{game[y[0]+1]}")
                    elif game[y[0]+3] == "g":
                        currentGreenCount = int(f"{y[1]}{game[y[0]+1]}")
                else:
                    if game[y[0]+2] == "b":
                        currentBlueCount = int(y[1])
                    elif game[y[0]+2] == "r":
                        currentRedCount = int(y[1])
                    elif game[y[0]+2] == "g":
                        currentGreenCount = int(y[1])
            #check if to many balls used
            if currentRedCount > RED:
                invalidGames.append(line[0])
            elif currentGreenCount > GREEN:
                invalidGames.append(line[0])
            elif currentBlueCount > BLUE:
                invalidGames.append(line[0])
        print(f"Game {line[0]} Red:{currentRedCount} Blue:{currentBlueCount} Green: {currentGreenCount}")
print(f"Invalid Games: {invalidGames}")
sum = 0
for game in enumerate(lines, start=1):
    if game[0] not in invalidGames:
        sum += game[0]
print(f"Total Sum: {sum}")

