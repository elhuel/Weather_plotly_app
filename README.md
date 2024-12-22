## **Quickstart**

Follow these steps to get your project up and running:

### 1. **Clone the Repository**

First, clone the project repository to your local machine using the following command:

```bash
git clone https://github.com/elhuel/Weather_plotly_app.git
```

### 2. **Install Required Libraries using "pip"**

```bash
pip install Flask requests plotly
```

### 3. **API Key**:
   - Obtain an API key from AccuWeather.
   - Create a file named `api_key.json` in the root directory with the following structure:
     ```json
     {
       "API_KEY": "your_api_key_here"
     }
     ```
     
### 4. **Run app.py**

## **WeatherApp**

WeatherApp is a web application that provides weather forecasts for specified cities. It allows users to input city names and receive detailed weather information, including temperature, wind speed, and precipitation probabilities. The application also visualizes this data through interactive graphs.

### **Features**

- **City Search**: Users can input one or more cities to get weather forecasts.
- **Forecast Duration**: Users can specify the number of days for which they want the weather forecast (1, 5, or 10 days).
- **Weather Conditions**: The application retrieves and displays:
  - Maximum temperature
  - Wind speed
  - Precipitation probability
- **Data Visualization**: Interactive graphs are generated to visualize temperature, wind speed, and precipitation probabilities over the specified duration.

### **Technologies Used**

- **Flask**: A lightweight WSGI web application framework for Python.
- **Requests**: A simple HTTP library to make API calls.
- **Plotly**: A graphing library for creating interactive plots.
- **HTML/CSS**: For frontend design.

### **Installation**

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd WeatherApp
   ```

2. **Install dependencies**:
   Make sure you have Python installed. Then install the required packages using pip:
   ```bash
   pip install Flask requests plotly
   ```

3. **API Key**:
   - Obtain an API key from AccuWeather.
   - Create a file named `api_key.json` in the root directory with the following structure:
     ```json
     {
       "API_KEY": "your_api_key_here"
     }
     ```

### **Usage**

1. **Run the application:**
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:8000`.

3. Enter the name of the city or cities you want to check the weather for, select the number of days, and submit the form.

### Example Input

- City: London
- Additional Cities: New York, Tokyo
- Days: 5 days

### Output

The application will display a summary of the weather conditions for each city along with interactive graphs showing:

- Temperature trends over the specified days.
- Wind speed trends.
- Precipitation probability trends.

### Error Handling

The application includes error handling for various scenarios:

- Invalid city names or API request failures will return appropriate error messages.
- Users are informed if no data is available for their requested cities.
