def save_satellite_image(lat, lon):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={lon},{lat}&z=15&l=sat"
    
    response = requests.get(map_request)
    
    with open("satellite_image.png", "wb") as file:
        file.write(response.content)

# Пример использования
save_satellite_image(55.7558, 37.6173)
