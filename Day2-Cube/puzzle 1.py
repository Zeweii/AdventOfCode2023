# read input file 

# read line by line 

# split after ':'

# split using ; as delimiter

#     split using , as delimter

#     if contains red, green or blue, increment value to corresponding colour

#     compare, number should not contain more than target value cubes

# add game id

import re

def main():
    sum = 0
    with open("Day2-Cube\cubes.txt", 'r') as file:
        for id, line in enumerate(file, 1):
            line = line.rstrip()
            cleaned_line = re.split('[:,; ]', line)
            cleaned_line.pop(0)
            cleaned_line.pop(0)
            content = [value for value in cleaned_line if value.strip()]
            l, c = list_split(content)
            if check_line_cubes(l, c):
                sum = sum + content
        print(sum)

def check_line_cubes(ints, colours):
    # red = 12, blue = 14, green = 13
    flag = True
    for dex, element in enumerate(ints, 0):
        if int(element) >= 15:
            flag = False
            break
        if int(element) == 14 and colours[dex] != "blue":
            flag = False
            break
        if int(element) == 13 and colours[dex] == "red":
            flag = False
            break
    return flag

def list_split(list):
    return list[::2], list[1::2]

if __name__ == "__main__":
    main()