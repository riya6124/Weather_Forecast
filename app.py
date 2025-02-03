from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "your api key"  # Replace with your actual OpenWeatherMap API key

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&cnt=7&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
        if weather_data.get('cod') != '200':  # Check for successful response
            error_message = weather_data.get('message', 'Error fetching weather data.')
            return render_template('index.html', error_message=error_message)
    else:
        weather_data = None
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)


