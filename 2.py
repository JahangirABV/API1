import requests
import math

# Функция для вычисления расстояния между двумя точками
def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000  # 111 километров в метрах
    a_lon, a_lat = a
    b_lon, b_lat = b

    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)

    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    distance = math.sqrt(dx * dx + dy * dy)
    return distance

# Пример последовательности координат
points = [(55.7566, 37.6222), (55.7583, 37.6589), (55.7500, 37.6400)]

# Создаем строку для меток
marks = '~'.join([f"{lon},{lat}" for lat, lon in points])

# Запрос к API Яндекс.Карт
map_request = f"http://static-maps.yandex.ru/1.x/?ll=37.6173,55.7558&spn=0.1,0.1&l=map&pt={marks},pm2rdm"
response = requests.get(map_request)

# Сохраняем карту в файл
with open("map_path.png", "wb") as file:
    file.write(response.content)

# Вычисляем общую длину пути
total_distance = sum(lonlat_distance(points[i], points[i + 1]) for i in range(len(points) - 1))
print(f"Общая длина пути: {total_distance:.2f} метров")
