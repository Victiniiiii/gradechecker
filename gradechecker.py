import time
import winsound
import datetime
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

login_url = "https://kimlik.ege.edu.tr/Identity/Account/Login?ReturnUrl=%2F"
grade_url = "https://kimlik.ege.edu.tr/Redirect/Redirect?AppEncId=z3Td%2Fth1x8vcvHw%2BDyN0G7GVy9eklCUQxjzDjMFwZaI%3D"
driver = webdriver.Firefox()
driver.maximize_window()

username = input("Enter your username: ")
password = input("Enter your password: ")
os.system('cls' if os.name == 'nt' else 'clear') # clears the console for privacy

def login(driver, username, password):
    driver.get(login_url)
    time.sleep(2)  
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys(username)
    time.sleep(random.randint(1, 3))  
    password_field.send_keys(password)
    time.sleep(random.randint(1, 3)) 
    password_field.send_keys(Keys.RETURN)
    time.sleep(5) 

def check_for_changes(driver, initial_html):    
    current_html = driver.page_source
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_html != initial_html:
        print(f"Changes detected at {current_time}!")
        if os.name == 'nt':  # Windows
            while True:
                winsound.Beep(300, 500)  # frequency and duration 
        else:  # macOS
            while True:
                os.system('say "beep"')
    else:
        print(f"No changes detected at {current_time}.")


login(driver, username, password)
driver.get(grade_url)
time.sleep(5)
initial_html = driver.page_source
start_time = time.time()

while True:
    check_for_changes(driver, initial_html)
    driver.get(grade_url)    
    time.sleep(random.randint(30, 60))
    
    if time.time() - start_time > random.randint(1500, 1700):  
        print("Reloginning!")
        login(driver, username, password)
        driver.get(grade_url)
        time.sleep(5)
        start_time = time.time()
