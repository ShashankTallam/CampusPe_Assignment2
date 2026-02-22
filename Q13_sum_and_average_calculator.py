
from collections import Counter


def sum_average_calculator():
    try:
        # Asking the for specific numbers to enter
        count = int(input("How many numbers? "))

        #  list to store all input numbers
        numbers_list = []

        
        for i in range(1, count + 1):
            num = float(input(f"Enter number {i}: "))
            numbers_list.append(num)

        #  required calculations
        total_sum = sum(numbers_list)
        average = total_sum / count
        maximum = max(numbers_list)
        minimum = min(numbers_list)

        sorted_numbers = sorted(numbers_list)
        mid = count // 2
        if count % 2 == 1:
            median = sorted_numbers[mid]
        else:
            median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2

        frequency = Counter(numbers_list)
        highest_count = max(frequency.values())
        if highest_count == 1:
            mode_result = "No mode"
        else:
            mode_values = sorted([num for num, freq in frequency.items() if freq == highest_count])
            mode_result = mode_values[0] if len(mode_values) == 1 else mode_values

        # Displaying the result
        print("Sum:", total_sum)
        print("Average:", average)
        print("Maximum:", maximum)
        print("Minimum:", minimum)
        print("Median:", median)
        print("Mode:", mode_result)

    # invalid input 
    except Exception:
        print("Invalid input.")

# calling the function
sum_average_calculator()