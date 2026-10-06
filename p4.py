#  Сума цифр числа
# Дано натуральне число N. Обчисліть суму його цифр.

def digit_sum(n):
    if n == 0:
        return 0

    return n % 10 + digit_sum(n // 10)


n = int(input("Введіть натуральне число: "))
print(digit_sum(n))