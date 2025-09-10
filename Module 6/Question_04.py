def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

test_list = [1, 2, 3, 4, 5]
result = sum_of_list(test_list)
print(f"The sum of the numbers in the list is: {result}")