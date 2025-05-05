#task 1

cities = ["Київ", "Одеса", "Львів", "Харків", "Житомир"]
city_set = set(cities)

for city in ["Одеса", "Полтава"]:
    if city in city_set:
        print(f"{city} є у списку.")
    else:
        print(f"{city} немає у списку.")


#task 2

students = {"Іван": 80, "Марія": 95, "Олег": 78, "Анна": 85}

name = input("Введіть ім'я студента: ")

try:
    print(f"Оцінка студента {name}: {students[name]}")
except KeyError:
    print("Студента з таким ім'ям не знайдено.")


#task 3

import random

numbers = [random.randint(1, 100) for _ in range(1000)]
counter = {}

for num in numbers:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1

most_common = max(counter.items(), key=lambda x: x[1])
print(f"Найчастіше число: {most_common[0]}, кількість повторень: {most_common[1]}")
