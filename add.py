# Розклад студентів на тиждень
# 3 групи, 5 днів, 4 пари

schedule = [
    # Група 1
    [
        ["ООП", "Математика", "Фізика", "Вільне вікно"],
        ["Англійська", "ООП", "Вільне вікно", "Проєктування ПЗ"],
        ["Дискретна математика", "Фізика", "ООП", "Математика"],
        ["ООП", "Вільне вікно", "Фізика", "Англійська"],
        ["Англійська", "Проєктування ПЗ", "ООП", "Фізкультура"]
    ],

    # Група 2
    [
        ["ООП", "Фізика", "Математика", "Вільне вікно"],
        ["Англійська", "ООП", "Математика", "Проєктування ПЗ"],
        ["Дискретна математика", "Фізика", "ООП", "Вільне вікно"],
        ["ООП", "Математика", "Фізика", "Англійська"],
        ["Англійська", "Проєктування ПЗ", "Вільне вікно", "Фізкультура"]
    ],

    # Група 3
    [
        ["ООП", "Математика", "Фізика", "Англійська"],
        ["Англійська", "ООП", "Вільне вікно", "Проєктування ПЗ"],
        ["Дискретна математика", "Фізика", "ООП", "Математика"],
        ["ООП", "Вільне вікно", "Фізика", "Англійська"],
        ["Англійська", "Проєктування ПЗ", "ООП", "Фізкультура"]
    ]
]


days = [
    "Понеділок",
    "Вівторок",
    "Середа",
    "Четвер",
    "П'ятниця"
]


# Вибір групи

group = int(input("Виберіть групу (1-3): ")) - 1

if group < 0 or group > 2:
    print("Такої групи немає")
    exit()


# Вивід розкладу обраної групи

print("\nРозклад групи", group + 1)

for day in range(5):

    print("\n" + days[day])

    for lesson in range(4):
        print(
            lesson + 1,
            "пара -",
            schedule[group][day][lesson]
        )


# 1. День з найбільшим навантаженням

max_lessons = 0
max_day = 0

for day in range(5):

    lessons = 0

    for lesson in range(4):

        if schedule[group][day][lesson] != "Вільне вікно":
            lessons += 1

    if lessons > max_lessons:
        max_lessons = lessons
        max_day = day


print("\n------------------------------")
print("День з найбільшим навантаженням")
print("------------------------------")

print(
    days[max_day],
    "-",
    max_lessons,
    "пар"
)


# 2. День з незручним розкладом
# Шукаємо дні, де є "Вільне вікно"

print("\n------------------------------")
print("Дні з вікнами")
print("------------------------------")

found_window = False

for day in range(5):

    for lesson in range(4):

        if schedule[group][day][lesson] == "Вільне вікно":

            print(
                days[day],
                "- вільне вікно на",
                lesson + 1,
                "парі"
            )

            found_window = True


if not found_window:
    print("Днів з вікнами немає")


# 3. Перевірка занять для потоку

print("\n------------------------------")
print("Заняття для потоку")
print("------------------------------")

found_stream = False

for day in range(5):

    for lesson in range(4):

        checked_subjects = []

        for group1 in range(3):

            subject = schedule[group1][day][lesson]

            if subject == "Вільне вікно":
                continue

            if subject in checked_subjects:
                continue

            checked_subjects.append(subject)

            groups = []

            for group2 in range(3):

                if schedule[group2][day][lesson] == subject:
                    groups.append(group2 + 1)

            if len(groups) > 1:

                print(
                    days[day],
                    "-",
                    lesson + 1,
                    "пара -",
                    subject,
                    "- групи:",
                    groups
                )

                found_stream = True


if not found_stream:
    print("Занять для потоку немає")