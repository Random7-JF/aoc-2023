data = open("day3-test.input")
lines = data.readlines()
symCoords = []
numCoords = []
for line in enumerate(lines, start=1):
    for char in enumerate(line[1].strip(), start=1):
        if not char[1].isnumeric() and char[1] != ".":
            symCoords.append((line[0],char[0]))
        if char[1].isnumeric():
            numCoords.append((line[0],char[0]))
print(f"symCoords: {symCoords}")
print(f"numCoords: {numCoords}")

for symbol in symCoords:
    print(f"Symbol: {symbol}")
    