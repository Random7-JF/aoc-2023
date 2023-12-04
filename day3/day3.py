data = open("/home/random/projects/aoc-2023/day3/day3-test.input")
lines = data.read().splitlines()
#Get dimensions of grid
gridHeight = len(lines)
gridWidth = len(lines[0])
print(f"gridHeight: {gridHeight}, gridWidth: {gridWidth}")
#Scan grid for symbol
symbolCoords = set()
for rIndex, row in enumerate(lines):
    for cIndex, column in enumerate(row):
        if not column.isnumeric() and column != ".":
            symbolCoords.add((rIndex, cIndex))
#- Once symbol is found, scan all adjacent spots for a number, save their coordinate
for x, symbol in enumerate(symbolCoords):
    print(f"row: {lines[symbol[0]][symbol[1]]}")
    print(f"row: {lines[symbol[0]-x][symbol[1]]}")

#Scan through columns in coordinates to get whole numbers.
print(f"Symcoords {symbolCoords}")