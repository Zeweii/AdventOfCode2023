import math

def num_of_possible_button_hold_times(time_str, record_str):
    try:
        # Convert input strings to float
        time = float(time_str)
        record = float(record_str)

        min_button_hold_time = (-time + (time ** 2 - 4 * record) ** 0.5) / -2
        max_button_hold_time = (-time - (time ** 2 - 4 * record) ** 0.5) / -2

        # If both h1 and h2 are integers, we need to offset the result
        offset = int(min_button_hold_time == min_button_hold_time // 1 and max_button_hold_time == max_button_hold_time // 1) * 2

        min_button_hold_time = math.ceil(min_button_hold_time)
        max_button_hold_time = math.floor(max_button_hold_time)

        return max_button_hold_time - min_button_hold_time - offset + 1
    except ValueError:
        # Handle the case where conversion to float fails
        return None

def main():
    with open("Day5-Speedboat\input.txt", "r") as file:
        parameters = []

        for line in file:
            line = line.strip().split()
            parameters.append(line)

        # Check if the number of elements in both lists is the same
        if len(parameters[0]) != len(parameters[1]):
            print("Error: Unequal number of elements in input lists.")
            return

        parameters[0].pop(0)
        parameters[1].pop(0)
        print(parameters)
        product = 1

        for i in range(len(parameters[0])):
            result = num_of_possible_button_hold_times(parameters[0][i], parameters[1][i])
            product *= result
            print(product)

if __name__ == '__main__':
    main()
