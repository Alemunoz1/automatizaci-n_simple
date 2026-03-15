from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service("chromedriver.exe"), options=options)

empresa = "microsoft"

driver.get(f"https://www.google.com/search?q=precio+accion+{empresa}")

sleep(5)

try:
    empresa_nombre = driver.find_element(By.CSS_SELECTOR, "div.PZPZlf").text
    precio = driver.find_element(By.CSS_SELECTOR, "span[jsname='vWLAgc']").text

    print(f"{empresa_nombre}: ${precio}")

except:
    print("No se pudo obtener el precio de la acción en este momento.")

driver.quit()