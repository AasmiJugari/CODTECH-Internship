import requests
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# API URL (NO API KEY REQUIRED)
# ---------------------------
url = (
    "https://api.open-meteo.com/v1/forecast?"
    "latitude=19.0760&longitude=72.8777"
    "&hourly=temperature_2m,relativehumidity_2m"
)

# ---------------------------
# FETCH DATA
# ---------------------------
response = requests.get(url)
data = response.json()

# ---------------------------
# EXTRACT DATA
# ---------------------------
time = data["hourly"]["time"][:10]
temperature = data["hourly"]["temperature_2m"][:10]
humidity = data["hourly"]["relativehumidity_2m"][:10]

# ---------------------------
# VISUALIZATION
# ---------------------------
sns.set()

# Temperature Graph
plt.figure()
plt.plot(time, temperature)
plt.xticks(rotation=45)
plt.title("Hourly Temperature Forecast")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()

# Humidity Graph
plt.figure()
plt.bar(time, humidity)
plt.xticks(rotation=45)
plt.title("Hourly Humidity Levels")
plt.xlabel("Time")
plt.ylabel("Humidity (%)")
plt.tight_layout()
plt.show()
