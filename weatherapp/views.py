from django.shortcuts import render
import requests

def index(request):
    weather_data = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = '0748d89c053b8738e2196f99594406b4'  # 🔑 Replace with your OpenWeatherMap key
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        
        response = requests.get(url)
        data = response.json()

        if data.get('cod') == 200:
            weather_data = {
                'city': city.title(),
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'].title(),
                'country': data['sys']['country'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            weather_data = {'error': 'City not found. Please try again.'}
            
    return render(request, 'weatherapp/index.html', {'weather_data': weather_data})
