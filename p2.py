def add_item(inventory, item):
    for i in range(len(inventory)):
        if inventory[i] == "Empty":
            inventory[i] = item
            return

    print("Немає вільного місця")


def remove_item(inventory, item):
    for i in range(len(inventory)):
        if inventory[i] == item:
            inventory[i] = "Empty"
            return

    print("Предмет не знайдено")


def compact_inventory(inventory):
    new_inventory = []

    for item in inventory:
        if item != "Empty":
            new_inventory.append(item)

    while len(new_inventory) < 10:
        new_inventory.append("Empty")

    for i in range(len(inventory)):
        inventory[i] = new_inventory[i]


inventory = ["Empty"] * 10

print("Початковий інвентар:")
print(inventory)


add_item(inventory, "Sword")
add_item(inventory, "Potion")
add_item(inventory, "Shield")
add_item(inventory, "Bow")

print("\nПісля додавання предметів:")
print(inventory)


remove_item(inventory, "Potion")

print("\nПісля видалення Potion:")
print(inventory)


compact_inventory(inventory)

print("\nПісля ущільнення:")
print(inventory)