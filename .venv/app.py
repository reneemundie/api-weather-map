# Main app file to run the application
# Import statements for modules to use for the application
from flask import Flask, render_template, jsonify, json
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
import api as api

# Creating the application object
app = Flask(__name__, template_folder="templates")

# Variable to access API key stored separately for security
app.config.from_object('config')

# Creating the Google Maps object
GoogleMaps(app)

# Rendering the HTML template for the application to the landing page
@app.route('/')
def index():
    return render_template('index.html')

# Loading the Google Map object and route to /map path
@app.route('/map')
def mapview():
    map = Map(
        identifier = "England",
        lat = 52.10878488192114,
        lng = -1.75652590787354,
        zoom = 6,
        markers = { 
            icons.dots.blue: [
                ( 54.4609, -3.0886 ),
                ( 50.6395, -2.0566 ),
                ( 51.8330, -1.8433 ),
                ( 51.4545, -2.5879 ),
                ( 52.2053, 0.1218 ),
                ( 51.7520, -1.2577 ),
                ( 52.6309, -1.2974 ),
                ( 51.1789, -1.8262 ),
                ( 50.4429, -5.0553 ),
                ( 52.4862, -1.8904 ),
            ] 
        },
        style = "height:550px;width:850px;margin:0;color:#242f3e"
    )
    return render_template('map.html', map=map)

# Creating a variable to hold the weather data
weather_data = api.get_weather_data()

# Function to get the weather data in JSON format and route it to /data path
@app.route('/data')
def json_weather():
    return jsonify(weather_data)

# Function to format the JSON weather data to Python dictionary and route it to /pydata path
@app.route('/pydata')
def python_weather():
    weather_data = api.get_weather_data()
    return json.dumps(weather_data)

# Main function to run the application on port 8000
if __name__ == '__main__':
    app.run(debug=True, port=5000)