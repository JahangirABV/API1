cities_input = input("Введите города через запятую: ")
cities = [city.strip() for city in cities_input.split(",")]

coordinates = {
    "Москва": (55.7558, 37.6173),
    "Санкт-Петербург": (59.9343, 30.3351),
    "Сочи": (43.5853, 39.7203),
}

southern_city = min(coordinates.keys(), key=lambda city: coordinates[city][0])
print(f"Самый южный город: {southern_city}")
