import folium
import random
import requests

cities = ["Санкт-Петербург", "Казань", "Калининград", "Владивосток"]

def get_city_coordinates(city):
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    geocode_params = {
        "geocode": city,
        "format": "json",
        "apikey": "0d997e8f-b415-4fd0-91b1-c9547916c893"
    }
    response = requests.get(geocode_url, params=geocode_params).json()
    try:
        point = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        coords = tuple(map(float, point.split()))
        return coords
    except (KeyError, IndexError):
        print(f"Не удалось получить координаты для города {city}")
        return None

def create_city_map(coords, filename="city_map.html"):
    city_map = folium.Map(location=[coords[0], coords[1]], zoom_start=12)

    folium.Marker(location=[coords[0], coords[1]]).add_to(city_map)

    city_map.save(filename)
    print(f"Карта города сохранена в файл {filename}")

def guess_the_city():
    random.shuffle(cities)

    for city in cities:
        print(f"Показывается карта города. Угадай город!")

        coords = get_city_coordinates(city)
        if not coords:
            continue

        create_city_map(coords, f"?_map.html")

        input("Нажмите Enter, чтобы увидеть следующий город...")

        user_guess = input("Введите ваш ответ: ").strip()
        if user_guess.lower() == city.lower():
            print("Правильный ответ!")
        else:
            print(f"Неправильно! Это был {city}.")

guess_the_city()
