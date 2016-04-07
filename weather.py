# Python 3 only?
import requests
import json
import sys
import datetime

# Your OpenWeatherMap Api Key
APPID = "aab0e21de127f26fd689163ee765fe5a";
CITY = sys.argv[1]
UNITS = "metric" # metric, imperial

def req_weather():
    request = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + CITY + "&APPID=" + APPID + "&units=" + UNITS)
    weather = json.loads(request.text)
    return weather

def print_weather():
    weather = req_weather()

    sunrise = datetime.datetime.fromtimestamp(
    weather["sys"]["sunrise"]).strftime('%Y-%m-%d %H:%M:%S'
    )

    sunset = datetime.datetime.fromtimestamp(
    weather["sys"]["sunset"]).strftime('%Y-%m-%d %H:%M:%S'
    )

    print(weather["name"], ", ", weather["sys"]["country"])
    print("\n")
    print("Temperature: ", weather["main"]["temp_min"], " C")
    print("\n")
    print("Sunrise at: ",  sunrise)
    print("\n")
    print("Sunset at: ", sunset)


def main():
    weather = req_weather()

    if len(sys.argv) < 2:
        print("Usage: ./weather [city_name]")
        sys.exit()

    if weather["cod"] != 200:
        print(weather["message"])
        sys.exit()

    print_weather()


if __name__ == "__main__":
    main()
