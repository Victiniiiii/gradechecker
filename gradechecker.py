from selenium import webdriver
import time
import winsound
import datetime

# tam yarım saatte bi kickliyo, düzelt

# otomatik login yapması lazım, ama kullanıcı adı ve şifreyi kaydetmesin, ve mac icin de winsound alternatifi
login_url = "https://kimlik.ege.edu.tr/Identity/Account/Login?ReturnUrl=%2F"
grade_url = "https://kimlik.ege.edu.tr/Redirect/Redirect?AppEncId=z3Td%2Fth1x8vcvHw%2BDyN0G7GVy9eklCUQxjzDjMFwZaI%3D"
driver = webdriver.Firefox()

def check_for_changes(driver, initial_html):    
    current_html = driver.page_source
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_html != initial_html:
        print(f"Changes detected at {current_time}!")
        while True:
            winsound.Beep(300, 500)  # frequency and duration 
    else:
        print(f"No changes detected at {current_time}.")

driver.get(login_url)
input("Please log in and press any key.")
driver.get(grade_url)
time.sleep(5)
initial_html = driver.page_source

# for loop x30 ?? ama random da kullansın, 15-60 saniye arası sürelerle refreshlesin, ama tam 25-30dklık sürede yeni session açsın
# belki yeni sessionu yan sekmede açıp sekme değişebilir ama zorlar bi tık gereksiz gibi 

while True:
    check_for_changes(driver, initial_html)
    driver.get(grade_url)
    time.sleep(59)
