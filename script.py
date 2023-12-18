from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import tempfile
import shutil
import time

nombre_de_votes = 0

while True:
    try:
        repertoire_temporaire = tempfile.mkdtemp()
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument(f"--user-data-dir={repertoire_temporaire}")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(
            "https://player.qualifio.com/20/1C356AA8-C157-45A4-BDCD-11403078D38C/s210/v1.cfm?id=1C356AA8-C157-45A4-BDCD-11403078D38C&pdomain=https://www.nordlittoral.fr&_init_fpic=1"
        )

        elem = driver.find_element(By.CSS_SELECTOR, "input#jouer")
        elem.click()
        elem = driver.find_element(By.CSS_SELECTOR, "div#answerVPic_9163012")
        elem.click()
        elem = driver.find_element(By.CSS_SELECTOR, "input#suivant1")
        elem.click()
        nombre_de_votes += 1
        print(f"Grâce à toi, Gisèle a gagné {nombre_de_votes} votes")
    
    finally:
        driver.close()
        shutil.rmtree(repertoire_temporaire)
