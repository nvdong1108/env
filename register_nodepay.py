
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from faker import  Faker
from auto_disconnect_wifi import reset_wifi
import pyautogui
import time

fake  = Faker()

mail = fake.email()
userName = fake.user_name()
password = "P@ssw0rd1108"
time_sleep = 2
time_sleep_before = 1
time_sleep_after = 2
loop  = 0
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
        #email
        typing_input(823,396,mail)
        #userName
        typing_input(823,450,userName)
        #pw
        typing_input(823,506,password)
        #cf pw
        typing_input(823,611,password)
        #tick đồng ý
        click_check_box(765,769,time_sleep_after)
        # check robot
        click_check_box(780,843,time_sleep_after*3)
        # click button register
        click_check_box(931,940,time_sleep_after*3)

        #back homepage
        click_check_box(953,721,time_sleep_after*3)
        #userName
        typing_input(866,531,mail)
        #password
        typing_input(868,581,password)
        #click robot
        click_check_box(778,707,time_sleep_after*2)
        #click login
        click_check_box(940,804,time_sleep_after*3)
        #click close popup like X
        click_check_box(1095,248,time_sleep_after*3)
        #click href add extention
        click_check_box(1131,148,time_sleep_after)
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

while loop < 10:
    loop+=1
    print("****************** begin ",loop, "******************")
    register()
    print("****************** end ",loop,"******************")
