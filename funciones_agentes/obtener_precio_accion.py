from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obtener_precio_accion(driver, consulta):

    driver.get(f"https://www.google.com/search?q=stock+{consulta}")

    try:
        empresa = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.PZPZlf"))
        ).text

        precio = driver.find_element(By.CSS_SELECTOR, "span[jsname='vWLAgc']").text

        return f"{empresa}: ${precio}"

    except:
        return "No se pudo obtener el precio de la acción en este momento."