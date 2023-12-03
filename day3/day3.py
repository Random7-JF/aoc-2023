data = open("day3-test.input")
lines = data.readlines()
SYMBOLS = "*#$+"
symCoords = []
numCoords = []
for line in enumerate(lines):
    for char in enumerate(line[1].strip()):
        if char[1] in SYMBOLS:
            print(f"found symbol at {line[0]},{char[0]} - {char[1]}")
            symCoords.append((line[0],char[0]))
        if char[1].isnumeric():
            print(f"Found number at {line[0]},{char[0]} - {char[1]}")
            numCoords.append((line[0],char[0]))
print(f"symCoords: {symCoords}")
print(f"numCoords: {numCoords}")