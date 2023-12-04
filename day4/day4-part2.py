data = open("/home/random/projects/aoc-2023/day4/day4-test.input")
lines = data.read().splitlines()
scores = []
winCards = []
for i, line in enumerate(lines, start=1):
    card = line.split("|")
    winnerCard = card[0].replace(f"Card {i}:", "").strip().split(" ")
    playerCard = card[1].strip().split(" ")
    score = 0
    for pick in playerCard:
        if pick.isnumeric() and pick in winnerCard:
                if score == 0:
                    score = 1
                elif score != 0:
                    score = score *2
    scores.append(score)

print(f"Score {sum(scores)}")
#Store copies after each game
#Card 1 wins 4 times
#add to list 2,3,4,5
#check card# to list and run count more times?