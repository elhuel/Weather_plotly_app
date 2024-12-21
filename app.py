from flask import Flask, render_template, request
import requests
import json
from weather import *
from flask import jsonify
import plotly.graph_objs as go
import plotly.io as pio

# Load API key from JSON file
with open('api_key.json', 'r') as file:
    data = json.load(file)

api_key = data["API_KEY"]

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    cities = []
    responses = []
    
    if request.method == 'POST':
        city = request.form['city']
        cities.append(city)
        additional_cities = request.form.getlist('additional_city')
        cities.extend(additional_cities)
        days = request.form['days']
        weather_data = {}

        for city in cities:
            response = get_conditions(api_key, city, days)

            if isinstance(response, str) and response.startswith("Request error"):
                return jsonify({"error": response}), 400
            elif isinstance(response, str):
                print(response)
                return jsonify({"error": "An unexpected error occurred while fetching weather data."}), 500
            
            weather_data[city] = response

        if days == "1":
            weather_summary = []
            for city, data in weather_data.items():
                conditions = data[0]
                summary = f"Город: {city}\n" \
                          f"Дата: {conditions['date']}\n" \
                          f"Температура: {conditions['temperature']}°C\n" \
                          f"Скорость ветра: {conditions['wind']} км/ч\n" \
                          f"Вероятность осадков: {conditions['precipitation_probability']}%\n"
                weather_summary.append(summary)

            return render_template('result.html', weather_summary=weather_summary)

        graphs = []
        for city, data in weather_data.items():
            dates = [entry['date'] for entry in data]
            temperatures = [entry['temperature'] for entry in data]
            wind_speeds = [entry['wind'] for entry in data]
            precipitation_probabilities = [entry['precipitation_probability'] for entry in data]

            fig_temp = go.Figure()
            fig_temp.add_trace(go.Scatter(x=dates, y=temperatures, mode='lines+markers', name=f'Temperature in {city}'))
            fig_temp.update_layout(title=f'Temperature Forecast for {city}', xaxis_title='Date', yaxis_title='Temperature (°C)')

            fig_wind = go.Figure()
            fig_wind.add_trace(go.Scatter(x=dates, y=wind_speeds, mode='lines+markers', name=f'Wind Speed in {city}'))
            fig_wind.update_layout(title=f'Wind Speed Forecast for {city}', xaxis_title='Date', yaxis_title='Wind Speed (km/h)')

            fig_precip = go.Figure()
            fig_precip.add_trace(go.Bar(x=dates, y=precipitation_probabilities, name=f'Precipitation Probability in {city}'))
            fig_precip.update_layout(title=f'Precipitation Probability for {city}', xaxis_title='Date', yaxis_title='Probability (%)')

            graphs.append({
                'temp_graph': pio.to_json(fig_temp),
                'wind_graph': pio.to_json(fig_wind),
                'precip_graph': pio.to_json(fig_precip)
            })

        return render_template('result.html', graphs=graphs)

    return render_template('form_beta.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)