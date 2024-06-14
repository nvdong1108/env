import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from faker import  Faker

from FileHandler import FileHandler
from disconnect_wifi import reset_wifi
import pyautogui
import time

fake  = Faker()



time_sleep = 2
time_sleep_before = 1
time_sleep_after = 2
loop  = 0

def get_password():
    return fake.password(10,special_chars=True,upper_case=True, lower_case=True,digits=True)

def click_check_box(x,y,sleep):
    pyautogui.moveTo(x,y)
    time.sleep(time_sleep_before)
    pyautogui.click()
    time.sleep(sleep)
def typing_input(x,y,value):
    pyautogui.moveTo(x,y)
    time.sleep(time_sleep_before)
    pyautogui.click()
    pyautogui.write(value)
    time.sleep(time_sleep_after)
def register():
    try:
        time.sleep(1)
        mail = fake.email()
        userName = fake.user_name()
        password = get_password()
        log = "mail : "+mail+" , userName : "+userName +" , pw : "+password
        FileHandler.add_data(log)
        print(log)

        print("to page nodepay extention then install")
        #click button  thêm extention vao chrome
        click_check_box(1407,240,time_sleep_after)
        #click popup continue install
        click_check_box(1019,240,time_sleep_after)
        #click popup add extention
        click_check_box(1027,236,time_sleep_after)
        #click manager extention
        click_check_box(1771,59,time_sleep_after)
        #click extention nodepay
        click_check_box(1592,307,time_sleep_after)
        #click extention nodepay
        click_check_box(1577,425,time_sleep_after)
        #click xoa extention nodepay
        click_check_box(1403,239,time_sleep_after)
        #click confrom remove  extention nodepay
        click_check_box(1597,216,time_sleep_after)

        print("Register Sucess begin change IP address...........")
        time.sleep(3)
        reset_wifi()
        time.sleep(5)
        print("success")
    finally:
        print("end")


userName = f"{fake.user_name()}{random.randint(1980, 2010)}"
print(userName)
