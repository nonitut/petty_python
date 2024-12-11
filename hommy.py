# Задание: "Поиск медианы в двух отсортированных массивах"
# Условие:
# Даны два отсортированных массива A и B, каждый из которых содержит n элементов. Необходимо найти медиану объединенного массива, который состоит из элементов обоих массивов.

# Определение медианы:
# - Если общее количество элементов объединенного массива четное, медиана — это среднее значение двух центральных элементов.
# - Если общее количество элементов нечетное, медиана — это центральный элемент.

# Пример:
# A = [1, 3]
# B = [2]
# # Объединенный массив: [1, 2, 3]
# # Медиана: 2

# A = [1, 2]
# B = [3, 4]
# # Объединенный массив: [1, 2, 3, 4]
# # Медиана: (2 + 3) / 2 = 2.5

# Требования:
# 1. Реализуйте функцию find_median_sorted_arrays(A: List[int], B: List[int]) -> float, которая принимает два отсортированных массива и возвращает медиану объединенного массива.
# 2. Ваша функция должна работать за O(log(min(n, m))), где n и m — длины массивов A и B соответственно.

# ### Подсказки:
# - Используйте бинарный поиск для нахождения медианы.
# - Определите, какой из массивов меньше, и работайте с ним, чтобы уменьшить количество операций.
# - На каждом шаге определяйте, корректно ли выбраны границы для медианы, и корректируйте их при необходимости.

# ### Пример реализации:

# def find_median_sorted_arrays(A, B):
#     # Убедимся, что A - это меньший массив
#     if len(A) > len(B):
#         A, B = B, A

#     n, m = len(A), len(B)
#     total_left = (n + m + 1) // 2
#     left, right = 0, n

#     while left <= right:
#         partition_A = (left + right) // 2
#         partition_B = total_left - partition_A

#         max_left_A = A[partition_A - 1] if partition_A > 0 else float('-inf')
#         min_right_A = A[partition_A] if partition_A < n else float('inf')

#         max_left_B = B[partition_B - 1] if partition_B > 0 else float('-inf')
#         min_right_B = B[partition_B] if partition_B < m else float('inf')

#         if max_left_A <= min_right_B and max_left_B <= min_right_A:
#             if (n + m) % 2 == 0:
#                 return (max(max_left_A, max_left_B) + min(min_right_A, min_right_B)) / 2
#             else:
#                 return max(max_left_A, max_left_B)
#         elif max_left_A > min_right_B:
#             right = partition_A - 1
#         else:
#             left = partition_A + 1

#     raise ValueError("Input arrays are not sorted")

# # Примеры использования:
# print(find_median_sorted_arrays([1, 3], [2]))  # Вывод: 2.0
# print(find_median_sorted_arrays([1, 2], [3, 4]))  # Вывод: 2.5

# from typing import List  — это строка, которая используется в Python для поддержки аннотации типов 
# Она импортирует тип List из модуля typing, который позволяет явно указывать тип данных, с которыми работает функция. 

# медиана - в математике число по середине

from typing import List

def find_median_sorted_arrays(A: List[int], B: List[int]) -> float:
    if len(A) > len(B):  # Убедимся, что работаем с меньшим массивом, def - функция, array - массив;
        A, B = B, A      # Функция len() в Python используется для получения длины (количества элементов)

    n, m = len(A), len(B)
    total_left = (n + m + 1) // 2  # Количество элементов в левой половине
    left, right = 0, n

    while left <= right:
        partition_A = (left + right) // 2
        partition_B = total_left - partition_A

        max_left_A = A[partition_A - 1] if partition_A > 0 else float('-inf')  # Граничные элементы
        min_right_A = A[partition_A] if partition_A < n else float('inf')

        max_left_B = B[partition_B - 1] if partition_B > 0 else float('-inf')
        min_right_B = B[partition_B] if partition_B < m else float('inf')

        # Проверяем, корректно ли выбрана точка разделения
        if max_left_A <= min_right_B and max_left_B <= min_right_A:  # Если общее количество элементов четное
            if (n + m) % 2 == 0:
                return (max(max_left_A, max_left_B) + min(min_right_A, min_right_B)) / 2  # Если нечетное
            else:
                return max(max_left_A, max_left_B)
        elif max_left_A > min_right_B:  # Сдвигаем границы бинарного поиска влево
            right = partition_A - 1
        else:  # Сдвигаем границы бинарного поиска вправо
            left = partition_A + 1

    raise ValueError("Input arrays are not sorted")  # Если входные массивы некорректны


# Пример использования:
result = find_median_sorted_arrays([1, 3], [2])
print(result)  # Ожидаемый вывод: 2.0

result = find_median_sorted_arrays([1, 2], [3, 4])
print(result)  # Ожидаемый вывод: 2.5