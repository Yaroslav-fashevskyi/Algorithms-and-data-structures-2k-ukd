#Точна степінь двійки
#Дано натуральне число N. Виведіть слово YES, якщо число N є точним степенем двійки, або слово NO в іншому випадку.
#Не використовуйте функцію піднесення до степеня!

def power_of_two(n):
    if n == 1:
        return True

    if n % 2 != 0:
        return False

    return power_of_two(n // 2)


n = int(input("вВедіть натуральне число: "))

if power_of_two(n):
    print("YES")
else:
    print("NO")