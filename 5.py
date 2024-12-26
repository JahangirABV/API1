def find_nearest_pharmacy(address):
    api_key = 'YOUR_API_KEY' 
    geocode_url = f"https://geocode-maps.yandex.ru/1.x?geocode={address}&apikey={api_key}&format=json"
    
    response = requests.get(geocode_url)
    location_data = response.json()
    
    if location_data['response']['GeoObjectCollection']['featureMember']:
        coords = location_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        lat, lon = map(float, coords.split())
        
        search_url = f"https://search-maps.yandex.ru/v1/?apikey={api_key}&text=аптека&ll={lon},{lat}&spn=0.01,0.01"
        
        search_response = requests.get(search_url)
        nearest_pharmacy = search_response.json()['features'][0]['properties']['name']
        
        print(f"Ближайшая аптека: {nearest_pharmacy}")

address_input = input("Введите адрес: ")
find_nearest_pharmacy(address_input)
