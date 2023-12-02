inputFile = open("input", "r")

total = 0
for line in inputFile.readlines():
    digits = [i for i in line.strip() if i.isdigit()]
    num = int(digits[0] + digits[-1])
    total += num

print(total)
