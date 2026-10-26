
import random


def generate_array(length, min_value, max_value):
    array = []

    for i in range(length):
        array.append(random.randint(min_value, max_value))

    return array


def print_array(array):
    print("{", end="")

    for i in range(len(array)):
        print(f"[cell - {i},value - {array[i]}]", end="")

        if i != len(array) - 1:
            print(",", end="")

    print("}")


def bubble_sort(array, direction):

    arr = array.copy()
    n = len(arr)

    for i in range(n - 1):

        for j in range(n - 1 - i):

            if direction:
                # За зростанням
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

            else:
                # За спаданням
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def insertion_sort(array, direction):


    arr = array.copy()

    for i in range(1, len(arr)):

        current = arr[i]
        j = i - 1

        if direction:

            # За зростанням
            while j >= 0 and arr[j] > current:
                arr[j + 1] = arr[j]
                j -= 1

        else:

            while j >= 0 and arr[j] < current:
                arr[j + 1] = arr[j]
                j -= 1

        arr[j + 1] = current

    return arr


def selection_sort(array, direction):

    arr = array.copy()
    n = len(arr)

    for i in range(n - 1):

        selected_index = i

        for j in range(i + 1, n):

            if direction:
                if arr[j] < arr[selected_index]:
                    selected_index = j

            else:
                if arr[j] > arr[selected_index]:
                    selected_index = j

        arr[i], arr[selected_index] = arr[selected_index], arr[i]

    return arr
