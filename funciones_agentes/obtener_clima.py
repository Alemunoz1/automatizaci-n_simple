from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obtener_clima(driver, consulta):

    driver.get(f"https://www.google.com/search?q=clima+{consulta}")

    try:
        temperatura = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "wob_tm"))
        ).text

        ciudad = driver.find_element(By.ID, "wob_loc").text
        clima = driver.find_element(By.ID, "wob_dc").text

        return f"El clima en {ciudad} es {clima} con {temperatura}°C."

    except:
        return "No se pudo obtener el clima en este momento."