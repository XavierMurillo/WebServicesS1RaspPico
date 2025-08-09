import network
import time

#Funcion para conectarse a WiFi
def connect(SSID, PASS, led):
    #Conectar a wifi
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    time.sleep(1)
    wlan.connect(SSID,PASS)
    intentos = 0

    #Se espera una conexion a la red
    while not wlan.isconnected() and intentos < 60:
        print("Conexion estableciendose...")
        time.sleep(0.5)
        intentos = intentos + 1

    #Verificacion de la conexion a red con un LED
    if wlan.isconnected():
        print(f"Conexion a la red {SSID} establecida")
        ip = wlan.ifconfig()[0]
        print(f"IP de la rasp pico w: {ip}")
        led.on()
        return True
    else:
        print(f"Error de conexion {wlan.status()}")
        return False