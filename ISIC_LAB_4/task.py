import requests
import matplotlib.pyplot as plt
import numpy as np

# Weather codes for open-meteo API (for later usage)
weather_codes = {
    (0,): "czyste niebo",
    (1,): "głównie bezchmurnie",
    (2,): "częściowo pochmurno",
    (3,): "pochmurno",
    (45,): "mgła",
    (48,): "opadająca mgła szronowa",
    (51,): "mżawka lekka",
    (53,): "mżawka umiarkowana",
    (55,): "mżawka gęsta",
    (56,): "zamrażająca mżawka: lekka",
    (57,): "zamrażająca mżawka: gęsta intensywność",
    (61,): "deszcz słaby",
    (63,): "deszcz umiarkowany",
    (65,): "deszcz intensywny",
    (66,): "marznący deszcz: intensywność lekka",
    (67,): "marznący deszcz: intensywność ciężka",
    (71,): "opady śniegu: intensywność niewielka",
    (73,): "opady śniegu: intensywność umiarkowana",
    (75,): "opady śniegu: intensywność duża",
    (77,): "ziarna śniegu",
    (80,): "przelotne opady deszczu: słabe",
    (81,): "przelotne opady deszczu: umiarkowane",
    (82,): "przelotne opady deszczu: gwałtowne",
    (85,): "opady śniegu lekkie",
    (86,): "opady śniegu intensywne",
    (95,): "burza: Słaba lub umiarkowana",
    (96,): "burza z lekkim gradem",
    (99,): "burza z silnym gradem",
}

# Coordinates for few places in the format (latitude, longitude)
coordinates = {
    "Gdynia": ("54.52", "18.53"),
    "Olsztyn": ("53.77995", "20.49416"),
    "Warszawa": ("52.237", "21.017"),
    "Nysa": ("50.46883", "17.33283"),
    "Opole": ("50.67211", "17.92533")
}

def fetch_hourly_weather(place, coords):
    weather_url = (f"https://api.open-meteo.com/v1/forecast"
                   f"?latitude={coords[0]}&longitude={coords[1]}"
                   f"&hourly=temperature_2m,rain,weather_code"
                   "&forecast_days=16"
                   "&past_days=14")

    print(f"Pogoda dla {place}: {weather_url}\n")
    place_weather = requests.get(weather_url).json()

    return place_weather

def plot_hourly_weather(place, place_weather):
    temperatures = place_weather["hourly"]["temperature_2m"]
    dates = place_weather["hourly"]["time"]

    plt.figure(figsize=(10,6))
    plt.plot(dates, temperatures, label='Temperatura (°C)')
    plt.title(f'Temperatura w {place} ({place_weather["latitude"]}, {place_weather["longitude"]})')
    plt.xlabel('Data')
    plt.ylabel('Temperatura (°C)')
    n = len(dates)
    step = max(1, n // 20)
    plt.xticks(np.arange(0, n, step))
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.savefig(place + ".png")
    plt.show()

def main():
    for place in coordinates:
        place_weather_hourly = fetch_hourly_weather(place, coordinates[place])
        plot_hourly_weather(place, place_weather_hourly)

if __name__ == '__main__':
    main()