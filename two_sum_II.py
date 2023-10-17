def twoSum( numbers, target):
    left_pointer = 0
    right_pointer = len(numbers) - 1
    while left_pointer < right_pointer:
        if numbers[left_pointer] + numbers[right_pointer] > target:
            right_pointer -= 1
        elif numbers[left_pointer] + numbers[right_pointer] < target:
            left_pointer += 1
        else:
            return [left_pointer + 1, right_pointer + 1]
    return []

numbers = [0, 1, 2, 7]
target = 9
print(twoSum(numbers, target))


        