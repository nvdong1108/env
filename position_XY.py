import pyautogui
from pynput import mouse, keyboard
import time
import os
# Danh sách lưu tọa độ
coordinates = []
log_path = os.path.join("logs" , "mouseInfoLog.txt")

def save_coordinates(x, y):
    coordinates.append((x, y))
    with open(log_path, "a") as file:
        file.write(f"{x},{y}\n")
    print(f"Tọa độ đã lưu: ({x}, {y})")
# Định nghĩa các hàm xử lý cho sự kiện chuột và bàn phím
def on_click(x, y, button, pressed):
    if pressed:
        save_coordinates(x, y)
def on_press(key):
    try:
        if key.char == 's':
            x, y = pyautogui.position()
            save_coordinates(x, y)
    except AttributeError:
        pass
# Thiết lập listener cho chuột và bàn phím

keyboard_listener = keyboard.Listener(on_press=on_press)

# Bắt đầu listener
keyboard_listener.start()

try:
    print("Nhấn phím 's' để lưu tọa độ hoặc nhấn Ctrl+C để dừng chương trình.")
    while True:
        x, y = pyautogui.position()
        print(f"Tọa độ hiện tại của con trỏ chuột: ({x}, {y})")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Đã dừng chương trình.")
    print("Danh sách tọa độ đã lưu:", coordinates)
finally:
    mouse_listener.stop()
    keyboard_listener.stop()
