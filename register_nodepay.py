from faker import Faker
import os
from FileHandler import FileHandler
from disconnect_wifi import reset_wifi
import pyautogui
import time
import random

fake = Faker()
time_sleep = 2
time_sleep_before = 1
time_sleep_after = 2
loop: int = 0
log_path = os.path.join("logs", "mouseInfoLog.txt")
coordinates_click = []
coordinates_typing = []


def load_x_y():
    global coordinates_click
    global coordinates_typing
    coordinates_click = []
    coordinates_typing = []

    with open(log_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(',')
            k = parts[0]
            x = int(parts[1])
            y = int(parts[2])
            if k == 'click':
                coordinates_click.append((x, y))
            else:
                coordinates_typing.append((x, y))
    print(f"list click {coordinates_click}")
    print(f"list typing {coordinates_typing}")



def get_password():
    return fake.password(10, special_chars=True, upper_case=True, lower_case=True, digits=True)


def click_check_box(index):
    print(f"click_check_box {index}")
    x, y = coordinates_click[index]
    pyautogui.moveTo(x, y)
    time.sleep(time_sleep_before)
    pyautogui.click()
    time.sleep(time_sleep_after)


def typing_input(index, value):
    print(f"typing_input {index}")
    x, y = coordinates_typing[index]
    pyautogui.moveTo(x, y)
    time.sleep(time_sleep_before)
    pyautogui.click()
    pyautogui.write(value)
    time.sleep(time_sleep_after)


def register():
    try:
        time.sleep(1)
        mail = fake.email()
        userName = f"{fake.user_name()}{random.randint(1980, 2010)}"
        password = get_password()
        index_click: int = -1
        index_typing: int = -1

        log = "mail : " + mail + " , userName : " + userName + " , pw : " + password
        FileHandler.add_data(log)
        print(log)
        print("====> PAGE 1. Register")
        print("1. typing mail")
        index_typing += 1
        typing_input(index_typing, mail)

        print("2. typing user name")
        index_typing += 1
        typing_input(index_typing, userName)

        print("3. typing password")
        index_typing += 1
        typing_input(index_typing, password)

        print("4. typing confirm password")
        index_typing += 1
        typing_input(index_typing, password)

        print("5. check agree")
        index_click += 1
        click_check_box(index_click)

        print("6. check not robot")
        index_click += 1
        click_check_box(index_click)

        print("6. click register")
        index_click += 1
        click_check_box(index_click)

        time.sleep(1000)

        print("====> PAGE 2. Notification register success")
        print("1. click come back homepage")
        index_click += 1
        click_check_box(index_click)

        print("====> PAGE 3. Login")
        print("1. typing mail")
        index_typing += 1
        typing_input(index_typing, mail)

        print("2. typing password")
        index_typing += 1
        typing_input(index_typing, mail)

        print("3. click not robot")
        index_click += 1
        click_check_box(index_click)

        print("4. click  Login")
        index_click += 1
        click_check_box(index_click)

        print("====> PAGE 4. Dashboard")
        # click close popup like X
        click_check_box(1095, 248)
        # click href add extention
        click_check_box(1131, 148)

        print("====> PAGE 4. Thêm extension")
        # click button  thêm extention vao chrome
        click_check_box(1407, 240)
        # click popup continue install
        click_check_box(1019, 240)
        # click popup add extention
        click_check_box(1027, 236)
        # click manager extention
        click_check_box(1771, 59)
        # click extention nodepay
        click_check_box(1592, 307)
        # click extention nodepay
        click_check_box(1577, 425)
        # click xoa extention nodepay
        click_check_box(1403, 239)
        # click confrom remove  extention nodepay
        click_check_box(1597, 216)

        print("Register Sucess begin change IP address...........")
        time.sleep(3)
        reset_wifi()
        time.sleep(5)
        print("success")
    finally:
        print("end")

def main() :
    while True:
        print(f"****************** begin ******************")
        register()
        print(f"****************** end  ******************")

load_x_y()
main()