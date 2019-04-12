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
    temp = round((dark_sky["daily"]["data"][1]["apparentTemperatureHigh"]-32)*5/9, 2)
    summery = dark_sky["currently"]["summary"]
    return render_template("index.html", temp = temp, forecast = summery)


if __name__ == "__main__":
    app.run(debug=True)
