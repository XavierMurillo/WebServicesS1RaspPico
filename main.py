from wifi_con import connect
from machine import Pin
import urequests

#Se usa el nombre y password de la red
SSID = "Entel_Murillo"
PASS = "M21081966XMS"
led = Pin("LED",Pin.OUT)
l1 = Pin(0, Pin.OUT)
l2 = Pin(1, Pin.OUT)
connect_status = False

#Se conecta a WIFI usando el codigo en wifi_con.py
while not connect_status:
    connect_status = connect(SSID, PASS, led)

#Funcion para obtener datos
def get_data():
    API_KEY = "$2a$10$aMlxrUfAjtPcSsarydUz6u1W7F5gNGiNtxPsq4yffnL.ty/8YqZAa"
    headers = {
    "X-Master-Key": API_KEY
    }
    url = 'https://api.jsonbin.io/v3/b/68827c1c7b4b8670d8a6cbca'
    local_url = 'http://192.168.100.12:5000/status' #Se debe usar la ip de la pc, no localhost o 127.0.0.1
    # data = urequests.get(url, headers = headers)
    data = urequests.get(local_url)
    res = data.json()
    data.close()
    # status = res.get("record").get("status", "desconocido")
    status = res.get("status")
    return status

while True:
    #Se lee datos JSON desde pastebin
    user_text = input("Ingrese la palabra datos para obtener la informacion mas reciente: ")
    if user_text == "datos":
        result = get_data()
        print(f"El status del sistema es \"{result}\"")
        if "bien" in result:
            l1.value(1)
            l2.value(0)
        elif "mal" in result:
            l1.value(0)
            l2.value(1)
        else:
            l1.value(0)
            l2.value(0) 