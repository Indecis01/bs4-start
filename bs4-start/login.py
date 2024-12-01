from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def login(url, driver, wait):
    driver.get(url)

    username = wait.until(EC.visibility_of_element_located((By.NAME, "A11")))  # Trouver le champ identifiant
    password = wait.until(EC.visibility_of_element_located((By.NAME, "A8")))  # Trouver le champ mot de passe

    username.send_keys("DANIEL")
    password.send_keys("DANIEL")

    first_button = wait.until(EC.element_to_be_clickable((By.NAME, "A9")))
    first_button.click()

    second_button = wait.until(EC.element_to_be_clickable((By.NAME, "A23")))
    second_button.click()
