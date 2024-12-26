import requests

# Координаты стадионов
stadiums_location = {
    "Лужники": (55.715551, 37.554191),
    "Спартак": (55.818015, 37.440262),
    "Динамо": (55.791540, 37.559809)
}

# Формируем строку для меток
marks = '~'.join([f"{lon},{lat}" for lat, lon in stadiums_location.values()])

# Запрос к API Яндекс.Карт
map_request = f"http://static-maps.yandex.ru/1.x/?ll=37.6173,55.7558&spn=0.1,0.1&l=map&pt={marks},pm2rdm"
response = requests.get(map_request)

# Сохраняем карту в файл
with open("map_moscow_stadiums.png", "wb") as file:
    file.write(response.content)
