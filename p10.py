import heapq
from collections import Counter
from itertools import count
from math import ceil, log2


def huffman(text):
    frequencies = Counter(text)
    if not frequencies:
        return {}

    order = count()
    heap = []

    for symbol, freq in frequencies.items():
        heapq.heappush(heap, (freq, next(order), symbol))

    # Побудова дерева Хаффмана
    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)

        heapq.heappush(
            heap, (f1 + f2, next(order), (left, right))
        )

    codes = {}

    # Формування кодів символів
    def build_codes(node, code=""):
        if isinstance(node, str):
            codes[node] = code or "0"
        else:
            build_codes(node[0], code + "0")
            build_codes(node[1], code + "1")

    build_codes(heap[0][2])

    return codes


text = input("Введіть текст: ")

codes = huffman(text)

encoded = "".join(codes[c] for c in text)

bits_per_symbol = max(1, ceil(log2(len(codes)))) if codes else 0

uniform_length = len(text) * bits_per_symbol
huffman_length = len(encoded)

print("\nТаблиця кодування:")
for symbol, freq in Counter(text).most_common():
    print(f"{symbol!r}: частота = {freq}, код = {codes[symbol]}")

print("\nЗакодований текст:", encoded)
print("Кількість символів:", len(text))
print("Унікальних символів:", len(codes))
print("Рівномірний код:", uniform_length, "біт")
print("Код Хаффмана:", huffman_length, "біт")

if uniform_length:
    saving = (1 - huffman_length / uniform_length) * 100
    print(f"Економія: {saving:.2f}%")