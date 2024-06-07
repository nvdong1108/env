from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui

# Thay đổi đường dẫn này
chrome_executable_path  = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  

extension_icon_x = 1737  # Thay đổi thành tọa độ X của biểu tượng
extension_icon_y = 64    # Thay đổi thành tọa độ Y của biểu tượng

extension_icon_x_2 = 200  # Tọa độ x muốn di chuyển đến khi làm xong việc  
extension_icon_y_2 = 400  # Tọa độ y muốn di chuyển đến khi làm xong việc  

# 1 hour = 60 giây * 60 phút = 3600 
time_one_hour = 60*60
time_sleep_loop =time_one_hour * 4

print(" thoi gian vòng lặp ", time_sleep_loop)

def click_extension_icon():
    try:
        print("begin 1235")
        pyautogui.moveTo(extension_icon_x, extension_icon_y,duration=1)
        print("doi 1s trước khi click")
        time.sleep(1)
        pyautogui.click()
        print("doi 10s click close popup")
        time.sleep(10)
        pyautogui.click()

        # di chuyển chuột đi ra chỗ khác
        pyautogui.moveTo(extension_icon_x_2, extension_icon_y_2,duration=1)
        print("di chuyển chuột đi ra chỗ khác")
        #pyautogui.mouseDown()
        #pyautogui.mouseUp()
        print("success time ",time.strftime("%Y-%m-%d %H:%M:%S"))
    except Exception as e:
        print(f"Failed to click extension icon: {e}")

# Vòng lặp đến chết
while True:
    click_extension_icon()
    time.sleep(time_sleep_loop)
