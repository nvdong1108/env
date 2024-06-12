import subprocess
import time
import requests

from FileHandler import FileHandler


def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        ip_info = response.json()
        return ip_info['ip']
    except requests.RequestException:
        return None

def disconnect_wifi():
    disconnect_command = "netsh wlan disconnect"
    subprocess.run(disconnect_command, shell=True)
def connect_wifi(ssid, password):
    # Lệnh kết nối lại Wi-Fi
    connect_command = f'netsh wlan connect name="{ssid}"'
    subprocess.run(connect_command, shell=True)
    time.sleep(5)
def reset_wifi():
    ssid = "OPPO Reno5"
    password = "12345678a"

    # Lấy IP trước khi ngắt kết nối
    ip_before = get_public_ip()
    log = "IP trước khi ngắt kết nối: "+ip_before
    print(log)
    FileHandler.log(log)
    print("Ngắt kết nối Wi-Fi...")
    disconnect_wifi()

    time.sleep(61)

    print("Kết nối lại Wi-Fi...")
    connect_wifi(ssid, password)

    # Lấy IP sau khi kết nối lại
    ip_after = get_public_ip()
    print("IP sau khi kết nối lại:", ip_after)
    FileHandler.log("IP sau khi kết nối lại: "+ip_after)
    if ip_before != ip_after:
        log = "Địa chỉ IP đã thay đổi. "+ip_before+" -> "+ ip_after
        print(log)
        FileHandler.log(log)
    else:
        log = "Địa chỉ IP không thay đổi."+ip_after
        print(log)

    print("Kết nối lại Wi-Fi Success")

if __name__ == "__main__":
    reset_wifi()
