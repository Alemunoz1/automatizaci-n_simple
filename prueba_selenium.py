from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Usa el ChromeDriver que descargaste manualmente
driver = webdriver.Chrome(service=Service("chromedriver.exe"))

# Abrir páginas web
driver.get("https://www.google.com")
sleep(2)
driver.get("https://hybridge.education")
sleep(2)
driver.get("https://openai.com")

# Cerrar el navegador
driver.quit()