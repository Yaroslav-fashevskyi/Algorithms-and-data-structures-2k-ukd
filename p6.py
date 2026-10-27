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
