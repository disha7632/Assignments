'''Write a Python function to get the largest number, smallest num and sum
of all from a list. '''

def get_largest_smallest_sum(numbers):
    if not numbers:
        return None, None, 0  # Return None for largest and smallest if the list is empty
    largest = smallest = numbers[0]
    total = 0
    for number in numbers:
        total += number
        if number > largest:
            largest = number
        elif number < smallest:
            smallest = number
    return largest, smallest, total

my_list = [12, 5, 23, 7, 42, 8, 19]

largest, smallest, total = get_largest_smallest_sum(my_list)

print("Largest number:", largest)
print("Smallest number:", smallest)
print("Sum of all numbers:", total)

