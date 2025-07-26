#  Weather Voice Assistant in Python

This Python project allows users to get **real-time weather information** for any city they input, and then reads the weather details aloud using **Windows PowerShell Text-to-Speech (TTS)**.

---

##  Features

- Get current weather details like:
  - 🌡️ Temperature (°C)
  - 🧊 Feels Like Temperature
  - 💨 Wind Speed (kph)
  - 🔵 Pressure (mb)
  - 💧 Humidity (%)
  - ☁️ Cloud Coverage (%)
  - 🔥 Heat Index (°C)
- Voice output using Windows `System.Speech.Synthesis`
- Uses [WeatherAPI](https://www.weatherapi.com/) for accurate, real-time weather data

---

##  Requirements

- Python 3.x  
- Windows OS (PowerShell is required for TTS)  
- Internet connection (for fetching weather data)

###  Python Libraries

Install the required Python library with:

```bash
pip install requests
```



##  How to Run

1. Clone or download this repository.
2. Replace the placeholder API key with your own in the script:
   ```python
   url = f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"
   ```
   Get a free key from [WeatherAPI](https://www.weatherapi.com/).
3. Run the script:

```bash
python weather_voice.py
```

4. Enter any city name when prompted.
5. The weather information will be printed on the screen and **spoken aloud**.

---

##  Example Output

```text
Enter the city name: Delhi
29.0
18.0
31.0
1005.0
65
55
36.0
(Speaking: The temperature in Delhi is 29 degrees celsius...)
```

---

##  Notes

- This script uses **PowerShell's `System.Speech.Synthesis`**, so it will work **only on Windows**.
- Avoid running this on macOS/Linux without modifying the TTS part.
- You can enhance this project by adding:
  - GUI with Tkinter or PyQt
  - Cross-platform TTS with `pyttsx3`
  - Weather forecasts for the next few days





