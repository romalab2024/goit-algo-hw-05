def binary_search(arr, target):
    """
    Реалізує двійковий пошук для відсортованого масиву.

    :param arr: Відсортований масив дробових чисел.
    :param target: Число, яке потрібно знайти.
    :return: Кортеж (кількість ітерацій, верхня межа).
    """
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            # Якщо знайдено точний збіг
            upper_bound = arr[mid]
            return iterations, upper_bound
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    # Якщо точного збігу немає, повертаємо верхню межу
    return iterations, upper_bound

# Приклад використання
sorted_array = [0.5, 1.2, 1.5, 2.3, 3.1, 4.8, 5.9]
target_value = 2.5

result = binary_search(sorted_array, target_value)
print(f"Кількість ітерацій: {result[0]}")
print(f"Верхня межа для числа {target_value}: {result[1]}")
