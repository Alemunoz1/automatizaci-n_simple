from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Configuración de Selenium
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
options.add_argument('--disable-blink-features=AutomationControlled')

# Usar tu chromedriver local
driver = webdriver.Chrome(service=Service("chromedriver.exe"), options=options)

# Abrir página
driver.get("https://openai.com")

sleep(3)

# Obtener texto del primer h2
texto = driver.find_element(By.CSS_SELECTOR, "h2").text

print(texto)

driver.quit()