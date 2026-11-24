import numpy as np
from numba import njit
from time import perf_counter
from statistics import mean

SIZES = [10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]


def generate(n):
    return np.random.randint(-10000, 10001, n, dtype=np.int16)


# Сортування підрахунком
@njit
def by_sort(a):
    counts = np.zeros(20001, dtype=np.int64)

    for x in a:
        counts[x + 10000] += 1

    result = np.empty(len(a), dtype=np.int16)
    p = 0

    for i in range(20000, -1, -1):
        for j in range(counts[i]):
            result[p] = i - 10000
            p += 1

    return result[5]


# Зберігання шести найбільших елементів
@njit
def by_top(a):
    top = np.full(6, -10001, dtype=np.int16)

    for x in a:
        if x > top[5]:
            j = 5

            while j > 0 and x > top[j - 1]:
                top[j] = top[j - 1]
                j -= 1

            top[j] = x

    return top[5]


# Шестиразовий пошук максимуму
@njit
def by_max(a):
    b = a.copy()

    for _ in range(6):
        index = 0

        for i in range(1, len(b)):
            if b[i] > b[index]:
                index = i

        value = b[index]
        b[index] = -10001

    return value


# Вимірювання часу виконання
def measure(method, a):
    start = perf_counter()
    result = method(a)
    end = perf_counter()

    return result, (end - start) * 1000


def main():
    methods = [by_sort, by_top, by_max]

    # Попередня компіляція алгоритмів
    sample = generate(100)

    for method in methods:
        method(sample)

    print("Порівняння ефективності алгоритмів")

    for n in SIZES:
        times = [[], [], []]

        print(f"\nКількість елементів: {n:,}")
        print("-" * 50)

        for run in range(3):
            a = generate(n)
            results = []

            for i, method in enumerate(methods):
                result, elapsed = measure(method, a)
                times[i].append(elapsed)
                results.append(result)

            assert len(set(results)) == 1

            print(f"Запуск №{run + 1}:")
            print(f"Шостий найбільший елемент: {results[0]}")
            print(f"Сортування: {times[0][-1]:.3f} мс")
            print(f"Масив: {times[1][-1]:.3f} мс")
            print(f"Максимуми: {times[2][-1]:.3f} мс")

            del a

        print("\nСередній час виконання:")
        print(f"Спосіб 1: {mean(times[0]):.3f} мс")
        print(f"Спосіб 2: {mean(times[1]):.3f} мс")
        print(f"Спосіб 3: {mean(times[2]):.3f} мс")

    print("\nУсі 45 вимірювань завершено.")


if __name__ == "__main__":
    main()