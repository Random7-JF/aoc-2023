data = open("/home/random/projects/aoc-2023/day4/day4-test.input")
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
    cardsWon = 0
    while numberOfCardsPerRound > 0:
        for pick in playerCard:
            if pick.isnumeric() and pick in winnerCard:
                cardsWon += 1
        numberOfCardsPerRound -= 1
    while cardsWon > 0:
        print(f"Index: {i} - cardsWon: {cardsWon} - Len: {len(wins)}")
        index = min(i+cardsWon, len(wins))
        wins[index] = wins[index]+1
        cardsWon -= 1
    print(f"Wins after game {i} - {wins}")
print(f"Wins: {sum(wins)}")