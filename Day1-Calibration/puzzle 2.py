# numbers_text = {
#     'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
# }

# def extract_numbers_from_string(s):
#     result = []
#     current_number = ''

#     for char in s:
#         if current_number in numbers_text:

#         if char.isalpha():
#             current_number += char
#             print("current number: ", current_number)
#         elif current_number:
#             result.extend(translate_word_to_digits(current_number))
#             current_number = ''

#         if char.isdigit():
#             result.append(char)

#     if current_number:
#         result.extend(translate_word_to_digits(current_number))
#     print("extractnumbersfrom string result: ", result)
#     return result

# def translate_word_to_digits(word):
#     result = []
#     for w in word.lower():
#         if w in numbers_text:
#             result.append(numbers_text[w])
#         else:
#             result.append(w)
#     print("result", result)
#     return result


# file_path = r"C:\\Users\\zacha\\OneDrive\\Documents\\AdventOfCode2023\\Day1-Calibration\\test.txt"

# with open(file_path, 'r') as f:
#     data = f.readlines()

# sum_result = 0

# for line in data:
#     numbers_list = extract_numbers_from_string(line)
#     print("numbers list: ", numbers_list)
    
#     if numbers_list:
#         integers_list = [int(num) for num in numbers_list if num.isdigit()]
#         # print("integers list: ", integers_list)
#         if integers_list:
#             value = str(integers_list[0]) + str(integers_list[-1])
#             sum_result += int(value)

# print("final sum:", sum_result)

ints = ["0","1","2","3","4","5","6","7","8","9"]

mapping = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"    
}


def main():
    sum = 0
    with open("C:\\Users\\zacha\\OneDrive\\Documents\\AdventOfCode2023\\Day1-Calibration\\calibration.txt",'r') as file:
        for each_line in file:
            sum = sum + get_ints_from_cal(each_line)
    print(sum)
    
    
def get_ints_from_cal(line):
    first = None
    last = None
    # line only has ints
    if line[0] in ints :
        first = line[0]
    if line[-1] in ints :
        last = line[-1]
        
    print("\n")
    indexes = []
    for key in mapping:
        
        if key in line:
            indexes.append((line.index(key),mapping[key]))
            print("first occ key:" , indexes)
            indexes.append((line.rindex(key),mapping[key]))
            print("last occ key:" , indexes)
    filtered_cal = [i for i in list(filter(filter_ints,line))]  
    print("filtered: ", filtered_cal)  
    for digit in filtered_cal:
        indexes.append((line.index(digit),digit)) #first occurence of digit
        print("first occ digit:" , indexes)
        indexes.append((line.rindex(digit),digit)) #last occurence of digit
        print("last occ digit:" , indexes)
    indexes = sorted(indexes)
    if first == None:
        first = indexes[0][1]
    if last == None:
        last = indexes[-1][1]
    combined = first + last
    return int(combined)
 
     
def filter_ints(line):
    return True if line in ints else False
  
  
if __name__ == "__main__":
     main()