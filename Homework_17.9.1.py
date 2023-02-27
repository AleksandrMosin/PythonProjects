def binary_search(num, target):
    """
    Реализация алгоритма двоичного поиска
    """
    left, right = 0, len(num) - 1
    while left <= right:
        mid = (left + right) // 2
        if num[mid] < target:
            left = mid + 1
        elif num[mid] > target:
            right = mid - 1
        else:
            return mid
    return left


def sort_nums(numbers):
    """
    Сортировка списка nums по возрастанию
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


input_nums = input("Введите последовательность чисел через пробел: ").split()
try:
    nums = [int(num) for num in input_nums]
except ValueError:
    print("Ошибка: вводите только числа, разделенные пробелами.")
    exit()

target_num = input("Введите любое число: ")
try:
    target_num = int(target_num)
except ValueError:
    print("Ошибка: введите число, а не строку.")
    exit()

sorted_nums = sort_nums(nums)
position = binary_search(sorted_nums, target_num)

print(f"Отсортированный список: {sorted_nums}")
print(f"Позиция элемента, который меньше введенного числа: {position - 1}")
print(f"Значение элемента на этой позиции: {sorted_nums[position - 1]}")
print(f"Позиция элемента, который больше или равен введенному числу: {position}")
print(f"Значение элемента на этой позиции: {sorted_nums[position]}")
