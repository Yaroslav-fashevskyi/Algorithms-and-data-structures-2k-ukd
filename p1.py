import random


# Генерація матриці випадкових чисел
def generate_matrix(m, n, min_value, max_value):
    matrix = []

    for i in range(m):
        row = []

        for j in range(n):
            row.append(random.randint(min_value, max_value))

        matrix.append(row)

    return matrix


# Вивід матриці
def print_matrix(matrix):
    if len(matrix) == 0:
        print("Матриця порожня")
        return

    if len(matrix[0]) == 0:
        print("Матриця порожня")
        return

    print("\t\t", end="")

    for j in range(len(matrix[0])):
        print(f"стовпець {j + 1}\t", end="")

    print()

    for i in range(len(matrix)):
        print(f"рядок {i + 1}\t", end="")

        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]}\t\t", end="")

        print()


# Вивід матриці з дробовими числами
def print_float_matrix(matrix):
    print("\t\t", end="")

    for j in range(len(matrix[0])):
        print(f"стовпець {j + 1}\t", end="")

    print()

    for i in range(len(matrix)):
        print(f"рядок {i + 1}\t", end="")

        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]:.2f}\t\t", end="")

        print()


# 1. Відняти від елементів кожного рядка
# середнє арифметичне цього рядка
def subtract_average(matrix):
    result = []

    for i in range(len(matrix)):
        sum_row = 0

        for j in range(len(matrix[i])):
            sum_row += matrix[i][j]

        average = sum_row / len(matrix[i])

        new_row = []

        for j in range(len(matrix[i])):
            new_row.append(matrix[i][j] - average)

        result.append(new_row)

    return result


# 2. Циклічний зсув на k позицій
# вправо та на k догори
def shift_matrix(matrix, k):
    m = len(matrix)
    n = len(matrix[0])

    result = []

    for i in range(m):
        result.append([0] * n)

    for i in range(m):
        for j in range(n):

            new_row = (i - k) % m
            new_column = (j + k) % n

            result[new_row][new_column] = matrix[i][j]

    return result


# 3. Видалити всі рядки і стовпці,
# які містять максимальний елемент
def remove_max_rows_columns(matrix):
    maximum = matrix[0][0]

    # Знаходимо максимальний елемент
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if matrix[i][j] > maximum:
                maximum = matrix[i][j]

    print("Максимальний елемент:", maximum)

    rows_to_delete = []
    columns_to_delete = []

    # Знаходимо всі рядки і стовпці,
    # де знаходиться максимальний елемент
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if matrix[i][j] == maximum:

                if i not in rows_to_delete:
                    rows_to_delete.append(i)

                if j not in columns_to_delete:
                    columns_to_delete.append(j)

    result = []

    # Створюємо матрицю без цих рядків і стовпців
    for i in range(len(matrix)):

        if i in rows_to_delete:
            continue

        new_row = []

        for j in range(len(matrix[i])):

            if j in columns_to_delete:
                continue

            new_row.append(matrix[i][j])

        result.append(new_row)

    return result


# 4. Поворот матриці на 90 градусів
# за годинниковою стрілкою
# без додаткового масиву
def rotate_90(matrix):
    n = len(matrix)

    # Транспонування матриці
    for i in range(n):
        for j in range(i + 1, n):

            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    # Перевертаємо кожен рядок
    for i in range(n):

        left = 0
        right = n - 1

        while left < right:

            temp = matrix[i][left]
            matrix[i][left] = matrix[i][right]
            matrix[i][right] = temp

            left += 1
            right -= 1


# Копія матриці
def copy_matrix(matrix):
    result = []

    for i in range(len(matrix)):
        result.append(matrix[i].copy())

    return result


# ==============================
# Основна частина програми
# ==============================

m = int(input("Введіть кількість рядків m: "))
n = int(input("Введіть кількість стовпців n: "))

min_value = int(input("Введіть мінімальне значення: "))
max_value = int(input("Введіть максимальне значення: "))


matrix = generate_matrix(m, n, min_value, max_value)


print("\n================================")
print("Початкова матриця")
print("================================")

print_matrix(matrix)


# ==============================
# Завдання 1
# ==============================

print("\n================================")
print("Завдання 1")
print("================================")
print("Віднімання середнього арифметичного кожного рядка:\n")

matrix_average = subtract_average(matrix)

print_float_matrix(matrix_average)


# ==============================
# Завдання 2
# ==============================

print("\n================================")
print("Завдання 2")
print("================================")

k = int(input("Введіть кількість позицій k: "))

matrix_shifted = shift_matrix(matrix, k)

print("\nМатриця після циклічного зсуву")
print("на", k, "позицій вправо та догори:\n")

print_matrix(matrix_shifted)


# ==============================
# Завдання 3
# ==============================

print("\n================================")
print("Завдання 3")
print("================================")

matrix_without_max = remove_max_rows_columns(matrix)

print("\nМатриця після видалення рядків")
print("і стовпців з максимальними елементами:\n")

print_matrix(matrix_without_max)


# ==============================
# Завдання 4
# ==============================

print("\n================================")
print("Завдання 4")
print("================================")

if m == n:

    matrix_rotated = copy_matrix(matrix)

    rotate_90(matrix_rotated)

    print("Матриця після повороту")
    print("на 90 градусів за годинниковою стрілкою:\n")

    print_matrix(matrix_rotated)

else:
    print("Для обертання in-place матриця повинна бути квадратною.")