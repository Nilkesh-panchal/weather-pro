import requests
import json
import os

city = input("Enter the city name: ")

url = f"http://api.weatherapi.com/v1/current.json?key=eb70c4e7107342658c5174958251707&q={city}"
r = requests.get(url)
# print(r.text)

json.loads(r.text)
weatherdic = json.loads(r.text)

json.loads(r.text)
winddic = json.loads(r.text)

json.loads(r.text)
feeldic = json.loads(r.text)

json.loads(r.text)
pressuredic = json.loads(r.text)

json.loads(r.text)
humiditydic = json.loads(r.text)

json.loads(r.text)
cloudydic = json.loads(r.text)

json.loads(r.text)
heatdic = json.loads(r.text)

print(weatherdic['current']['temp_c'])
print(winddic['current']['wind_kph'])
print(feeldic['current']['feelslike_c'])
print(pressuredic['current']['pressure_mb'])
print(humiditydic['current']['humidity'])
print(cloudydic['current']['cloud'])
print(heatdic['current']['heatindex_c'])   

cmd = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('the temperature in {city} is {weatherdic['current']['temp_c']} degrees celsius')"
os.system(cmd)

cmd = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('the wind speed in {city} is {winddic['current']['wind_kph']} degrees celsius')"
os.system(cmd)

cmd = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('the feels like temperature in {city} is {feeldic['current']['feelslike_c']} degrees celsius')"
os.system(cmd)

cmd = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('the pressure in {city} is {pressuredic['current']['pressure_mb']} millibars')"
os.system(cmd)

cmd = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('the humidity in {city} is {humiditydic['current']['humidity']} percent')"
os.system(cmd)  

cmd = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('the cloud coverage in {city} is {cloudydic['current']['cloud']} percent')"
os.system(cmd)

cmd = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('the heat index in {city} is {heatdic['current']['heatindex_c']} degrees celsius')"
os.system(cmd)
