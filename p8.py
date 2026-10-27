class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            replacement = node.right
            while replacement.left is not None:
                replacement = replacement.left
            node.value = replacement.value
            node.right = self._delete(node.right, replacement.value)
        return node

    def to_list(self):
        result = []

        def visit(node):
            if node is None:
                return
            visit(node.left)
            result.append(node.value)
            visit(node.right)

        visit(self.root)
        return result

    def minimum(self):
        current = self.root
        if current is None:
            return None
        while current.left is not None:
            current = current.left
        return current.value

    def maximum(self):
        current = self.root
        if current is None:
            return None
        while current.right is not None:
            current = current.right
        return current.value

    def count(self):
        return len(self.to_list())


if __name__ == '__main__':
    tree = BinaryTree()
    print('Порожнє дерево:', tree.to_list())
    for number in [50, 30, 70, 20, 40, 60, 80, 65, 70]:
        tree.insert(number)
    print('Після додавання:', tree.to_list())
    print('Знайти 40:', tree.search(40))
    print('Знайти 100:', tree.search(100))
    print('Найменший елемент:', tree.minimum())
    print('Найбільший елемент:', tree.maximum())
    print('Кількість елементів:', tree.count())

    tree.delete(20)  # без дітей
    print('Після видалення 20:', tree.to_list())
    tree.delete(60)  # одна дитина (65)
    print('Після видалення 60:', tree.to_list())
    tree.delete(50)  # двоє дітей (корінь)
    print('Після видалення 50:', tree.to_list())
    tree.delete(999)  # відсутній елемент
    print('Після видалення 999:', tree.to_list())
    print('Кількість після видалень:', tree.count())
