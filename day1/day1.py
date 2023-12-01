input = open("day1.input", "r")
data = input.readlines()

result = []
for line in range(len(data)):
    currentNumbers = []
    for char in data[line]:
        if char.isnumeric():
            currentNumbers.append(char)
    print(f"currentNumbers: {currentNumbers}")
    result.append(int(currentNumbers[0] + currentNumbers[len(currentNumbers)-1]))
print(f"result: {result}")
sum = 0
for num in result:
    sum += num
print(f"The sum of calibrations is: {sum}")
