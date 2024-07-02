import requests
import smtplib

to_email = "your email id"
Password = "your password"

OWN_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "c750267ea8190faf190f8b8003ff7b9c"
weather_params = {
    "lat": 'your latitude',
    "lon": 'your longitude',
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWN_endpoint, params=weather_params)
weather_data = response.json()

will_rain = False

for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 700:
        will_rain = True
if will_rain:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=to_email, password=Password)
    connection.sendmail(from_addr=to_email, to_addrs=to_email, msg="Subject:Rain Alert\n\nBring an Umbrella")
