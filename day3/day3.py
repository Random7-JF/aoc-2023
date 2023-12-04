data = open("/home/random/projects/aoc-2023/day3/day3-test.input")
lines = data.read().splitlines()
#Get dimensions of grid
gridHeight = len(lines)
gridWidth = len(lines[0])
#Scan grid for symbol
symbolCoords = set()
partNumbers = []
for rIndex, row in enumerate(lines):
    for cIndex, column in enumerate(row):
        if not column.isnumeric() and column != ".":
            #Add symbol to coord set
            symbolCoords.add((rIndex, cIndex))

#- Once symbol is found, scan all adjacent spots for a number, save their coordinate
for symbol in symbolCoords:
    #symbolCoords(Line, Char)
    for char in lines[symbol[0]]:
        adj = [0,1,-1]
        for x in adj:
            if (symbol[0] - x) >= 0 and (symbol[0] - x) <= len(lines) -1:
                print(f"char: {lines[symbol[0]-x][symbol[1]]} x:{x} symbol:{symbol}")
            if (symbol[1] - x) >= 0 and (symbol[1] - x) <= len(lines[symbol[0]]) -1:
                print(f"char: {lines[symbol[0]-x][symbol[1]]} x:{x} symbol:{symbol}")

    print("---------")