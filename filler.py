from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Indítsd el a böngészőt
driver = webdriver.Chrome()  # Győződj meg róla, hogy a ChromeDriver telepítve van

# Nyisd meg a Moodle bejelentkezési oldalt
driver.get("http://10.0.0.16:88/moodle/login/index.php")

# Találd meg a bejelentkezési mezőket, és töltsd ki őket
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys("kovacsp")
password.send_keys("Kokok777%")

# Nyomd meg a bejelentkezés gombot
login_button = driver.find_element(By.ID, "loginbtn")
login_button.click()

# Navigálj a teszthez
driver.get("http://10.0.0.16:88/moodle/course/view.php?id=11")

# Kattints a teszt indításához
start_test = driver.find_element(By.CLASS_NAME, "starttest")
start_test.click()

# Keress kérdéseket és válaszokat
# A kérdéseket egyedi módon kell kezelni, attól függően, hogyan épül fel a teszt

# Végül a teszt elküldése
submit_button = driver.find_element(By.NAME, "submit")
submit_button.click()

# Zárd be a böngészőt
driver.quit()
