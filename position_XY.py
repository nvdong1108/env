import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()
        print(f"Tọa độ hiện tại của con trỏ chuột: ({x}, {y})")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Đã dừng chương trình.")


