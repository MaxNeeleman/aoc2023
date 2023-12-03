with open("input") as f:
    data = f.read().strip()

data = (
    data.replace("one", "one1one")
    .replace("two", "two2two")
    .replace("three", "three3three")
    .replace("four", "four4four")
    .replace("five", "five5five")
    .replace("six", "six6six")
    .replace("seven", "seven7seven")
    .replace("eight", "eight8eight")
    .replace("nine", "nine9nine")
)

line = data.split("\n")

total = 0
for word in line:
    digits = [i for i in word.strip() if i.isdigit()]
    num = int(digits[0] + digits[-1])
    total += num

print(total)
