import pyautogui
from pynput import mouse, keyboard
import time
import os
# Danh sách lưu tọa độ
coordinates = []
log_path = os.path.join("logs" , "mouseInfoLog.txt")
shift_pressed = False

def clear_log_file():
    with open(log_path, "w") as file:
        file.truncate(0)
    print("Đã xóa dữ liệu trong file log.")
def save_coordinates(k,x, y):
    coordinates.append((k,x, y))
    with open(log_path, "a") as file:
        file.write(f"{k},{x},{y}\n")
    print(f"===========> lưu: ({k},{x}, {y})")

def on_press(key):
    global shift_pressed
    try:
        if key in (keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r):
            shift_pressed = True
        elif  key.char == 'c' and shift_pressed:
            shift_pressed = False
            x, y = pyautogui.position()
            save_coordinates('click', x, y)
        elif key.char == 't'and shift_pressed:
            shift_pressed = False
            x, y = pyautogui.position()
            save_coordinates('typing', x, y)
    except AttributeError:
        pass
# Thiết lập listener cho chuột và bàn phím

keyboard_listener = keyboard.Listener(on_press=on_press)

# Bắt đầu listener
keyboard_listener.start()

try:
    print("Nhấn phím 's' để lưu tọa độ hoặc nhấn Ctrl+C để dừng chương trình.")
    clear_log_file()
    while True:
        x, y = pyautogui.position()
        print(f"({x}, {y})")
        time.sleep(1)

except KeyboardInterrupt:
    print("Đã dừng chương trình.")
    print("Danh sách tọa độ đã lưu:", coordinates)
finally:
    keyboard_listener.stop()
