def get_district(address):
    api_key = 'YOUR_API_KEY'
    
    geocode_url = f"https://geocode-maps.yandex.ru/1.x?geocode={address}&apikey={api_key}&format=json"
    
    response = requests.get(geocode_url)
    location_data = response.json()
    
    if location_data['response']['GeoObjectCollection']['featureMember']:
        district_name = location_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['name']
        print(f"Район: {district_name}")

address_input = input("Введите адрес: ")
get_district(address_input)
