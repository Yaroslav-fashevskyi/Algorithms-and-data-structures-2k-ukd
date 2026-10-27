# Практична робота №6

### Код програми

```python
class Stack:
    def __init__(self):
        self.items = []
        self.top = -1

    def push(self, value):
        self.items.append(value)
        self.top += 1

    def pop(self):
        if self.top == -1:
            return None
        self.top -= 1
        return self.items.pop()

    def peek(self):
        if self.top == -1:
            return None
        return self.items[self.top]

    def clear(self):
        self.items.clear()
        self.top = -1

    def count(self):
        return len(self.items)

    def size(self):
        return len(self.items)

    def toString(self):
        return str(self.items)


stack = Stack()
print('Порожній стек:', stack.toString())
print('Кількість елементів:', stack.count())

stack.push(10)
stack.push(20)
stack.push(30)
print('Після додавання:', stack.toString())
print('Верхній елемент:', stack.peek())
print('Кількість елементів:', stack.count())
print('Розмір стека:', stack.size())

print('Видалений елемент:', stack.pop())
print('Стек після pop:', stack.toString())
print('Верхній елемент після pop:', stack.peek())

stack.clear()
print('Після очищення:', stack.toString())
print('Кількість після очищення:', stack.count())
print('pop з порожнього стека:', stack.pop())
print('peek з порожнього стека:', stack.peek())
```

### Результат виконання


```text
Порожній стек: []
Кількість елементів: 0
Після додавання: [10, 20, 30]
Верхній елемент: 30
Кількість елементів: 3
Розмір стека: 3
Видалений елемент: 30
Стек після pop: [10, 20]
Верхній елемент після pop: 20
Після очищення: []
Кількість після очищення: 0
pop з порожнього стека: None
peek з порожнього стека: None
```

### Скріншот результату

![img.png](img.png)

### Таблиця перевірки методів

| Метод | Що перевіряв | Результат |
|---|---|---|
| `push()` | Додавання 10, 20, 30 | `[10, 20, 30]` |
| `peek()` | Перегляд верхнього елемента | `30` |
| `pop()` | Видалення верхнього елемента | Повернув `30`, залишилось `[10, 20]` |
| `clear()` | Очищення стека | `[]` |
| `count()` | Кількість елементів до й після очищення | `3` і `0` |
| `size()` | Розмір стека після додавання | `3` |
| `toString()` | Виведення всіх елементів | `[10, 20, 30]` |
