import requests
import json
import sys
import time
#remember time somehow, files?

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
    print(weather["name"], ", ", weather["sys"]["country"])
    print("\n")
    print("Low: ", weather["main"]["temp_min"], " ºC")
    print("High: ", weather["main"]["temp_max"], " ºC")
    print("Clouds: ", weather["clouds"]["all"])
    print("\n")
    print("Sunrise at: ", time.localtime(weather["sys"]["sunrise"]))
    print("Sunset at: ", time.localtime(weather["sys"]["sunset"]))


def main():
    weather = req_weather()

    if len(sys.argv) < 2:
        print("Usage: ./weather [city_name]")
        sys.exit()

    if weather["cod"] == '404':
        print(weather["message"])
        sys.exit()

    print_weather()


if __name__ == "__main__":
    main()
