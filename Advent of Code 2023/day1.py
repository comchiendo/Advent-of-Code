file = open("input.txt", "r")

sum = 0
sum2 = 0
lines = file.readlines()

numlist = ["one", 
           "two", 
           "three", 
           "four", 
           "five", 
           "six", 
           "seven", 
           "eight", 
           "nine"]
for line in lines:
    p1_digits = []
    p2_digits = []
    for i, val in enumerate(line):
        if val.isdigit():
            p1_digits.append(val)
            p2_digits.append(val)
        for digit, value in enumerate(numlist):
            if line[i:].startswith(value):
                p2_digits.append(str(digit + 1))
    sum += int(p1_digits[0] + p1_digits[-1])
    sum2 += int(p2_digits[0] + p2_digits[-1])

print(sum)
print(sum2)