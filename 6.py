import random

cities_list = ["Москва", "Санкт-Петербург", "Казань", "Сочи"]
city_to_guess = random.choice(cities_list)

print(f"Угадайте город! Вот его часть: {city_to_guess[:2]}...")

user_guess = input("Ваш ответ: ")
if user_guess == city_to_guess:
    print("Правильно!")
else:
    print(f"Неправильно! Это был {city_to_guess}.")
