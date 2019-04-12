from flask import Flask, render_template, request
import requests

app = Flask(__name__)

dark_sky_api_key = "073ed950bcd367ad35e76ea60cf5511c"
ipstack_api_key = "55896dde6c19b26566166b446fe84094"

@app.route("/")
def index():

    current_location = requests.get("http://api.ipstack.com/check", params = {"access_key": ipstack_api_key}).json()
    lat = current_location["latitude"]
    lon = current_location["longitude"]
    dark_sky = requests.get("https://api.darksky.net/forecast/{}/{},{}".format(dark_sky_api_key, lat, lon)).json()

    return render_template("index.html", forecast =  dark_sky)


if __name__ == "__main__":
    app.run(debug=True)
