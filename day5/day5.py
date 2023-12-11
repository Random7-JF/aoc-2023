data = open("/home/random/projects/aoc-2023/day5/day5-test.input")
lines = data.read().splitlines()

seeds = []
seedToSoil = []
soilToFert = []
fertToWater = []
waterToLight = []
lightToTemp = []
tempToHumidity = []
humidityToLoc = []

def scanner(index, input, destination):
    scanner = True
    i = 1
    s = input[(min(index + i, len(input)))] 
    while scanner:
        if s != "" and ((index + i) <= (len(input)-1)):
            destination.append(s)
        else:
         scanner = False
        i += 1
        s = input[min(index + i, len(input)-1)] 


for index, line in enumerate(lines):
    s = line.split(":")
    if s[0] == "seeds":
        for c in s[1].strip().split(" "):
            seeds.append(c)
    elif s[0] == "seed-to-soil map":
        scanner(index, lines, seedToSoil)
    elif s[0] == "soil-to-fertilizer map":
        scanner(index, lines, soilToFert)
    elif s[0] == "fertilizer-to-water map":
        scanner(index, lines, fertToWater)
    elif s[0] == "water-to-light map":
        scanner(index, lines, waterToLight)
    elif s[0] == "light-to-temperature map":
        scanner(index, lines, lightToTemp)
    elif s[0] == "temperature-to-humidity map":
        scanner(index, lines, tempToHumidity)
    elif s[0] == "humidity-to-location map":
        scanner(index, lines, humidityToLoc)

print(f"Found seeds: {seeds}")
print(f"Found seed-to-soil: {seedToSoil}")
print(f"Found soil-to-fertilizer: {soilToFert}")
print(f"Found fertilizer-to-water: {fertToWater}")
print(f"Found water-to-light: {waterToLight}")
print(f"Found light-to-temperature: {lightToTemp}")
print(f"Found temperature-to-humidity: {tempToHumidity}")
print(f"Found humidity-to-location : {humidityToLoc}")


# seed-to-soil
# dest range | src range | range length

