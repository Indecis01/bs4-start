from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


def perform_actions(driver, wait):
    try:
        menu_item = wait.until(EC.visibility_of_element_located((By.ID, "M8")))
        actions = ActionChains(driver)
        actions.move_to_element(menu_item).perform()

        dropdown_item = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='tzM11']")))
        dropdown_item.click()

        next_button = wait.until(EC.element_to_be_clickable((By.ID, "A43")))
        next_button.click()

        company = wait.until(EC.visibility_of_element_located((By.NAME, "A13")))
        company.send_keys("SIGA SECURITE")

        display_company = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='A14']")))
        display_company.click()

        save_choice_company = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='A4']")))
        save_choice_company.click()

        data = []
        for y in range(210):
            while True:
                try:
                    table_container = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                                 "/html/body/form/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[3]/td/div/table/tbody/tr/td/div/div[2]/div[2]/table/tbody/tr/td/div/div[2]/div/table/tbody/tr[3]/td[1]/div")))

                    target_enroll = wait.until(
                        EC.visibility_of_element_located((By.XPATH, "//*[@id='ctzA4']/tbody/tr[3]/td[2]/div/div")))
                    target_enroll.click()

                    for i in range(10):
                        time.sleep(0.5)
                        row_table = wait.until(EC.visibility_of_element_located((By.ID, f"A4_{i+1}")))
                        row_table.click()

                        show_details_row = wait.until(EC.visibility_of_element_located((By.ID, "A20")))
                        show_details_row.click()

                        table_body_show_details = driver.find_element(By.XPATH, '//*[@id="A5_TB"]')

                        for tr in table_body_show_details.find_elements(By.XPATH, ".//tr"):
                            row = [item.text for item in tr.find_elements(By.XPATH, ".//td")]
                            if any(row):
                                data.append(row)
                                print(row)

                        row_ferme = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='A28']")))
                        row_ferme.click()

                except (TimeoutException, NoSuchElementException):
                    print("Aucun nouvel élément trouvé ou une étape a pris trop de temps.")
                    break

        # Convertir les données en DataFrame et les enregistrer dans un fichier Excel
        df = pd.DataFrame(data)
        df.to_excel("output.xlsx", index=False)
        print("Données enregistrées dans 'output.xlsx'")
        time.sleep(2)
        driver.quit()

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        driver.quit()
