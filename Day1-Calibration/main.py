
f = open(r"C:\\Users\\zacha\\OneDrive\\Documents\\AdventOfCode2023\\Day1-Calibration\\calibration.txt")
data = f.readlines()
sum = 0
for line in data:
    s = ''.join(x for x in line if x.isdigit())
    first = s[0]
    print("first: ", first)
    last = s[-1]
    print("last: ", last)
    number = first + last
    print(number)
    sum += int(number)
print("final sum: ", sum)
