import requests
import socket

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_info = response.json()
    return ip_info['ip']

def get_public_ip_with_proxy(proxy):
    proxies = {
        'http': proxy,
        'https': proxy
    }
    response = requests.get('https://api.ipify.org?format=json', proxies=proxies)
    ip_info = response.json()
    return ip_info['ip']

def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

# Không sử dụng proxy
print("Local IP:", get_local_ip())
print("Public IP:", get_public_ip())

# Sử dụng proxy
proxy = 'http://username:password@proxyserver:port'  # Thay thế bằng thông tin proxy của bạn
print("Public IP with Proxy:", get_public_ip_with_proxy(proxy))
