
import time
import pyautogui
import os
# 1 hour = 60 giây * 60 phút = 3600
time_sleep_loop =15
time_before_click =2
time_after_click =3
time_waiting_close =90
time_sleep_next_tasks =15
icons_coordinates = []

print(" thoi gian vòng lặp ", time_sleep_loop)
log_path = os.path.join("logs" , "mouseInfoLog.txt")
def click_icon(x,y) :
    pyautogui.moveTo(x, y,duration=1)
    time.sleep(time_before_click)
    pyautogui.click()
    time.sleep(time_after_click)
def load_x_y() :
    global icons_coordinates
    icons_coordinates = []
    with open(log_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            x, y = map(int, line.strip().split(','))
            icons_coordinates.append((x, y))
def click_extension_icon():
    try:
        for i in range(5):
            x, y = icons_coordinates[i]
            print(f"begin {i}")
            click_icon(x, y)
        time.sleep(180)
        print("success time ",time.strftime("%Y-%m-%d %H:%M:%S"))
    except Exception as e:
        print(f"Failed to click extension icon: {e}")
# Vòng lặp đến chết
def loop_click() :
    while True:
        click_extension_icon()
        time.sleep(1)
        #time.sleep(120)

load_x_y()
loop_click()

