import requests
from time import sleep
from datetime import datetime
from plyer import notification
from playsound import playsound


# Windows Notification
def notify(title, message, app_name):
    notification.notify(title=title, app_name=app_name, timeout=10, message=message)

notify('Prayertimes', 'App is running', 'Prayertimes')

# Formatting the current time
def current_time():
    time = datetime.now().time().strftime("%I:%M %p")
    time = time.split(":")
    time1 = str(int(time[0]))
    time2 = time[1]
    time = time1 + ":" + time2
    return time



print("Current time: " + current_time() + "\n")

ip = requests.get('https://api.ipify.org').text

with open("config.txt", "r", encoding="utf-8") as parameters_config:
    parameters = [line for line in parameters_config.readlines()]
    latitude = parameters[0].strip('\n').split('=')[1]
    longitude = parameters[1].strip('\n').split('=')[1]


# Extracting prayers data
link = "https://www.islamicfinder.us/index.php/api/prayer_times"
params = {
    "user_ip": ip,
    "latitude": f"{latitude}",
    "longitude": f"{longitude}",
    "method": '5'

}

response = requests.get(link, params=params)
data = response.json()


# Formatting prayer times
fajr: str = data["results"]["Fajr"]
fajr = f"{fajr.split('%')[0]}{fajr.split('%')[1].upper()}"

duha: str = data["results"]["Duha"]
duha = f"{duha.split('%')[0]}{duha.split('%')[1].upper()}"


duhr: str = data["results"]["Dhuhr"]
duhr = f"{duhr.split('%')[0]}{duhr.split('%')[1].upper()}"

asr: str = data["results"]["Asr"]
asr = f"{asr.split('%')[0]}{asr.split('%')[1].upper()}"

maghrib: str = data["results"]["Maghrib"]
maghrib = f"{maghrib.split('%')[0]}{maghrib.split('%')[1].upper()}"

isha: str = data["results"]["Isha"]
isha = f"{isha.split('%')[0]}{isha.split('%')[1].upper()}"


print(f"AL-Fajr: {fajr}")
print(f"AL- Duha: {duha}")
print(f"Al-Duhr: {duhr}")
print(f"AL- Asr: {asr}")
print(f"AL- Maghrib: {maghrib}")
print(f"AL- Isha: {isha}")


al_azan = (f'{__file__}Al-Azan.mp3'.replace("main.py",""))

keep_alive = True
while keep_alive:

    print(current_time() + " " + isha)

    if fajr == current_time():
        notify("Azan", "Time to pray Fajr", "Prayertimes")
        playsound(al_azan)
        sleep(60)
    elif duha == current_time():
        notify("Azan", "Time to pray Duha", "Prayertimes")
        playsound(al_azan)
        sleep(60)
    elif duhr == current_time():
        notify("Azan", "Time to pray Duhr", "Prayertimes")
        playsound(al_azan)
        sleep(60)
    elif asr == current_time():
        notify("Azan", "Time to pray Asr", "Prayertimes")
        playsound(al_azan)
        sleep(60)
    elif maghrib == current_time():
        notify("Azan", "Time to pray Maghrib", "Prayertimes")
        playsound(al_azan)
        sleep(60)
    elif isha == current_time():
        notify("Azan", "Time to pray Isha", "Prayertimes")
        playsound(al_azan)
        sleep(60)
    elif current_time() == current_time():
        playsound(al_azan)
        sleep(60)

    else:
        sleep(60)