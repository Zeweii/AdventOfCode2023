# read input file 

# read line by line 

# split after ':'

# split using ; as delimiter

#     split using , as delimter

#     if contains red, green or blue, increment value to corresponding colour

#     compare, number should not contain more than target value cubes

# add game id

import re
from math import prod

def main():
    sum = 0
    sum_of_powers = 0
    cubeLimit = { "red": 12, "blue": 14, "green":13}
    with open("Day2-Cube\cubes.txt", 'r') as file:
        lines = file.read().splitlines()
        for id, line in enumerate(lines):
            reds = [int(m) for m in re.findall(r"(\d+) red", line)]
            greens = [int(m) for m in re.findall(r"(\d+) green", line)]
            blues = [int(m) for m in re.findall(r"(\d+) blue", line)]

            redMax = max(reds)
            greenMax = max(greens)
            blueMax = max(blues)

            isPossible = (
                redMax <= cubeLimit["red"]
                and greenMax <= cubeLimit["green"]
                and blueMax <= cubeLimit["blue"]
            )

            if isPossible:
                sum += id + 1

            power = redMax * greenMax * blueMax
            sum_of_powers += power
    print(sum_of_powers)

if __name__ == "__main__":
    main()