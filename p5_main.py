import random
import time
from p3 import bubble_sort, insertion_sort, selection_sort


def partition(arr, left, right, direction):
    pivot = arr[(left + right) // 2]
    i = left
    j = right

    while i <= j:
        if direction:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
        else:
            while arr[i] > pivot:
                i += 1
            while arr[j] < pivot:
                j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    return i, j


def quick_sort_part(arr, left, right, direction):
    if left >= right:
        return

    i, j = partition(arr, left, right, direction)

    if left < j:
        quick_sort_part(arr, left, j, direction)
    if i < right:
        quick_sort_part(arr, i, right, direction)


def quick_sort(array, direction):
    arr = array.copy()

    if len(arr) > 1:
        quick_sort_part(arr, 0, len(arr) - 1, direction)

    return arr


def is_sorted(array, direction):
    for i in range(len(array) - 1):
        if direction:
            if array[i] > array[i + 1]:
                return False
        else:
            if array[i] < array[i + 1]:
                return False

    return True


def compare_sorts(sizes=(1_000, 10_000, 100_000)):
    algorithms = [
        ("QuickSort", quick_sort),
        ("Bubble Sort", bubble_sort),
        ("Insertion Sort", insertion_sort),
        ("Selection Sort", selection_sort)
    ]

    random.seed(42)

    for size in sizes:
        numbers = [round(random.uniform(-1000, 1000), 2) for i in range(size)]
        print(f"\nМасив: {size:,} елементів".replace(",", " "))

        for direction in (True, False):
            direction_name = "за зростанням" if direction else "за спаданням"
            print(f"\n{direction_name.capitalize()}")
            print(f"{'Алгоритм':<18} {'Час (с)':>12} {'Перевірка':>10}")
            print("-" * 42)

            expected = sorted(numbers, reverse=not direction)

            for name, sort_function in algorithms:
                print(f"{name:<18} ", end="", flush=True)

                start = time.perf_counter()
                result = sort_function(numbers, direction)
                seconds = time.perf_counter() - start

                correct = is_sorted(result, direction) and result == expected
                status = "OK" if correct else "ПОМИЛКА"
                print(f"{seconds:>12.3f} {status:>10}", flush=True)


if __name__ == "__main__":
    numbers = [3.14, -2.5, 0, 9.4, 3.14, -7.125]

    print("Приклад сортування:")
    print("Початковий масив:", numbers)
    print("За зростанням:   ", quick_sort(numbers, True))
    print("За спаданням:    ", quick_sort(numbers, False))

    print("\nПорівняння часу сортування:")
    compare_sorts()
