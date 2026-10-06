# Від A до B
# Дано два цілих числа A і В. Виведіть всі числа від A до B включно, в порядку зростання, якщо A < B, або в порядку спадання в іншому випадку.

def print_numbers(a, b):
    print(a, end=" ")

    if a == b:
        return

    if a < b:
        print_numbers(a + 1, b)
    else:
        print_numbers(a - 1, b)


a = int(input("Введіть ціле число A: "))
b = int(input("Введіть ціле число B: "))

print_numbers(a, b)