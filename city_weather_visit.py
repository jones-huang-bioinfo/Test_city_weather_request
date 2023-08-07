import requests
while True:
    city=input('please type in your city name, and then click \'Enter\'\n')
    if not city:
        break
    try:
        req=requests.get('https://api.tomorrow.io/v4/weather/realtime?location=%s&apikey=5ywvdh1ELyW4P7ja7wF6NE8DbtE1o0Tp'%city)
        print(req)
        print(req.text)
    except:
        print('failed to request local temperature')
        break
    dic_city=req.json()
    city_data=dic_city.get('data')
    if city_data:
        city_cloudy=city_data['values']
        print(city_cloudy.get('humidity'))
        print(city_cloudy.get('temperature'))
    else:
        print('inaccessible')

