import subprocess
import time
def disconnect_wifi():
    disconnect_command = "netsh wlan disconnect"
    subprocess.run(disconnect_command, shell=True)
def connect_wifi(ssid, password):
    # Lệnh kết nối lại Wi-Fi
    connect_command = f'netsh wlan connect name="{ssid}"'
    subprocess.run(connect_command, shell=True)
    time.sleep(5)
def reset_wifi():
    ssid = "wowcns_13f_5G"
    password = "83150425"

    print("Ngắt kết nối Wi-Fi...")
    disconnect_wifi()

    time.sleep(5)

    print("Kết nối lại Wi-Fi...")
    connect_wifi(ssid, password)

    print("Kết nối lại Wi-Fi Success")

if __name__ == "__main__":
    reset_wifi()
