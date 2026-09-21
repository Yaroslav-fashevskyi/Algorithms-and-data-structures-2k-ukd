import random


def generate_array(length, min_value, max_value):
    array = []

    for i in range(length):
        array.append(random.randint(min_value, max_value))

    return array


# 1
def task1(array, start, end):
    count = 0
    total = 0

    for i in range(start, end + 1):
        if array[i] % 2 == 0:
            count += 1
            total += array[i]

    return count, total


# 2
def task2(array):
    total = 0

    for number in array:
        total += number

    average = total / len(array)

    count = 0

    for number in array:
        if number > average:
            count += 1

    return average, count


# 3
def task3(array1, array2):
    result = []

    for i in range(len(array1)):
        result.append(array1[i] + array2[i])

    return result


# 4
def task4(array1, array2):
    result = []

    for number in array1:
        result.append(number)

    for number in array2:
        result.append(number)

    return result


# 5
def task5(array):
    min_index = 0
    max_index = 0

    for i in range(1, len(array)):
        if array[i] < array[min_index]:
            min_index = i

        if array[i] > array[max_index]:
            max_index = i

    temp = array[min_index]
    array[min_index] = array[max_index]
    array[max_index] = temp


# 6
def task6(array):
    positive = []
    negative = []

    for number in array:
        if number > 0:
            positive.append(number)
        elif number < 0:
            negative.append(number)

    return positive, negative


# 7
def task7(array):
    minimum = min(array)
    maximum = max(array)

    result = []

    min_added = False
    max_added = False

    for number in array:
        if number == minimum:
            if not min_added:
                result.append(number)
                min_added = True

        elif number == maximum:
            if not max_added:
                result.append(number)
                max_added = True

        else:
            result.append(number)

    return result


def average(array):
    total = 0

    for number in array:
        total += number

    return total / len(array)


# 8
def task8(array1, array2):
    average1 = average(array1)
    average2 = average(array2)

    min_average = min(average1, average2)
    max_average = max(average1, average2)

    result = []

    for number in array1:
        if min_average <= number <= max_average:
            result.append(number)

    for number in array2:
        if min_average <= number <= max_average:
            result.append(number)

    return result


print("Завдання 1")

array1 = generate_array(10, -10, 20)
print("Масив:", array1)

count, total = task1(array1, 2, 7)

print("Кількість парних:", count)
print("Сума парних:", total)


print("\nЗавдання 2")

array2 = generate_array(10, 0, 20)
print("Масив:", array2)

avg, count = task2(array2)

print("Середнє арифметичне:", avg)
print("Кількість більших за середнє:", count)


print("\nЗавдання 3")

array3_1 = generate_array(5, 0, 10)
array3_2 = generate_array(5, 0, 10)

print("Перший масив:", array3_1)
print("Другий масив:", array3_2)

print("Третій масив:", task3(array3_1, array3_2))


print("\nЗавдання 4")

array4_1 = generate_array(4, 0, 10)
array4_2 = generate_array(6, 0, 10)

print("Перший масив:", array4_1)
print("Другий масив:", array4_2)

print("Третій масив:", task4(array4_1, array4_2))


print("\nЗавдання 5")

array5 = generate_array(10, 0, 20)

print("До:", array5)

task5(array5)

print("Після:", array5)


print("\nЗавдання 6")

array6 = generate_array(10, -10, 10)

print("Масив:", array6)

positive, negative = task6(array6)

print("Додатні:", positive)
print("Від'ємні:", negative)


print("\nЗавдання 7")

array7 = generate_array(10, 0, 10)

print("До:", array7)
print("Після:", task7(array7))


print("\nЗавдання 8")

array8_1 = generate_array(6, 0, 20)
array8_2 = generate_array(6, 0, 20)

print("Перший масив:", array8_1)
print("Другий масив:", array8_2)

print("Середнє першого:", average(array8_1))
print("Середнє другого:", average(array8_2))

print("Третій масив:", task8(array8_1, array8_2))