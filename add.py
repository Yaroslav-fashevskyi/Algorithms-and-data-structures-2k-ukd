import json
import os


def compress(source, target):
    with open(source, "r", encoding="utf-8", newline="") as f:
        text = f.read()

    codes = huffman(text)
    encoded = "".join(codes[c] for c in text)

    padding = (8 - len(encoded) % 8) % 8
    encoded += "0" * padding

    data = bytes(
        int(encoded[i:i + 8], 2)
        for i in range(0, len(encoded), 8)
    )

    header = json.dumps({
        "codes": codes,
        "padding": padding
    }, ensure_ascii=False).encode("utf-8")

    with open(target, "wb") as f:
        f.write(len(header).to_bytes(4, "big"))
        f.write(header)
        f.write(data)

    print("Файл стиснено:", target)
    print("Початковий розмір:", os.path.getsize(source), "байт")
    print("Розмір архіву:", os.path.getsize(target), "байт")


def decompress(source, target):
    with open(source, "rb") as f:
        header_size = int.from_bytes(f.read(4), "big")
        header = json.loads(f.read(header_size))
        data = f.read()

    encoded = "".join(f"{byte:08b}" for byte in data)

    if header["padding"]:
        encoded = encoded[:-header["padding"]]

    reverse = {
        code: symbol
        for symbol, code in header["codes"].items()
    }

    result = []
    current = ""

    for bit in encoded:
        current += bit

        if current in reverse:
            result.append(reverse[current])
            current = ""

    with open(target, "w", encoding="utf-8", newline="") as f:
        f.write("".join(result))

    print("Файл розпаковано:", target)


while True:
    print("\n1. Стиснути файл")
    print("2. Розпакувати файл")
    print("0. Вихід")

    choice = input("Оберіть операцію: ")

    if choice == "1":
        compress(input("Шлях до файлу: "), "archive.huff")

    elif choice == "2":
        decompress(input("Шлях до архіву: "), "restored.txt")

    elif choice == "0":
        break