# Від 1 до n Дано натуральне число n. Виведіть всі числа від 1 до n.

def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n, end=" ")


n = int(input("Введіть натуральне число: "))
print_numbers(n)