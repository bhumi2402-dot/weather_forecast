from django.shortcuts import render
import requests
import datetime

def index(request):
    city = 'indore'  # default city
    exception_occured = False
    description = ''
    icon = '01d'
    temp = '--'
    
    if request.method == 'POST':
        city_input = request.POST.get('city', '').strip()
        if city_input:
            city = city_input

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5ffedb7a82a220f77a84de0db99eb3d1'
    params = {'units': 'metric'}

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200 and 'weather' in data:
            description = data['weather'][0]['description']
            icon = data['weather'][0]['icon']
            temp = data['main']['temp']
        else:
            exception_occured = True
            description = "City info not available."
            temp = '--'
            icon = '01d'
    except Exception:
        exception_occured = True
        description = "Error fetching data."
        temp = '--'
        icon = '01d'

    day = datetime.date.today()

    return render(request, 'index.html', {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'city': city,
        'exception_occured': exception_occured,
        'image_url': '/static/sunny-weather.jpg',
    })

