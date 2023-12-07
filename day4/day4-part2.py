data = open("/home/random/projects/aoc-2023/day4/day4.input")
lines = data.read().splitlines()
wins = dict()
for i, line in enumerate(lines,start=1):
    wins[i] = 1
print(f"Initial cards setup: {wins}")

for i, line in enumerate(lines, start=1):
    card = line.split("|")
    winnerCard = card[0].replace(f"Card {i}:", "").strip().split(" ")
    playerCard = card[1].strip().split(" ")
    numberOfCardsPerRound = wins[i]
    matches = 0
    gamewon = 0
    gamesPlayed = wins[i]
    while gamesPlayed > 0:
        for pick in playerCard:
            if pick.isnumeric() and pick in winnerCard:
                matches += 1
        while matches > 0:
            index = i+matches
            current = wins[index]
            print(f"Adding {i} to {current} : {wins[index]}")
            wins[index] = current + 1 #i = game number
            matches -= 1
        gamesPlayed -=1
    print(f"Game: {i} Matches: {matches} Gamewon: {gamewon}")
    print(f"Wins after game {i} - {wins}")
sum = sum(wins.values())
print(f"Sum: {sum}")