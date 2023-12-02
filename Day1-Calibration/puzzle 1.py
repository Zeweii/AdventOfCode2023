
f = open(r"C:\\Users\\zacha\\OneDrive\\Documents\\AdventOfCode2023\\Day1-Calibration\\calibration.txt")
data = f.readlines()
sum = 0
for line in data:
    s = ''.join(x for x in line if x.isdigit())
    first = s[0]
    last = s[-1]
    number = first + last
    sum += int(number)
print("final sum: ", sum)
