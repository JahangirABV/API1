home_address = input("Введите адрес дома: ")
university_address = input("Введите адрес университета: ")

def calculate_distance(home_coords, uni_coords):
    return lonlat_distance(home_coords, uni_coords)

# Предполагается получение координат через геокодер как в предыдущих примерах.
