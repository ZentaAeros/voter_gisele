from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

verif = True

while verif:
    driver = webdriver.Chrome()
    driver.get(
        "https://player.qualifio.com/20/1C356AA8-C157-45A4-BDCD-11403078D38C/s210/v1.cfm?id=1C356AA8-C157-45A4-BDCD-11403078D38C&pdomain=https://www.nordlittoral.fr&_init_fpic=1"
    )

    elem = driver.find_element(By.CSS_SELECTOR, "input#jouer")
    elem.click()
    elem = driver.find_element(By.CSS_SELECTOR, "div#answerVPic_9163012")
    elem.click()
    elem = driver.find_element(By.CSS_SELECTOR, "input#suivant1")
    elem.click()
    time.sleep(5)
    driver.close()
