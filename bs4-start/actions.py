from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

def perform_actions(driver, wait):
    menu_item = wait.until(EC.visibility_of_element_located((By.ID, "M8")))
    actions = ActionChains(driver)
    actions.move_to_element(menu_item).perform()

    dropdown_item = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='tzM11']")))
    dropdown_item.click()

    next_button = wait.until(EC.element_to_be_clickable((By.ID, "A43")))
    next_button.click()

    company = wait.until(EC.visibility_of_element_located((By.NAME, "A13")))
    company.send_keys("PUISSANCE 6")

    display_company = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='A14']")))
    display_company.click()

    save_choice_company = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='A4']")))
    save_choice_company.click()

    while True:
        try:
            table_container = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[3]/td/div/table/tbody/tr/td/div/div[2]/div[2]/table/tbody/tr/td/div/div[2]/div/table/tbody/tr[3]/td[1]/div")))

            for y in range(10):
                target_element = driver.find_element(By.XPATH, f"//*[@id='A4_{y+1}']")
                driver.execute_script("arguments[0].scrollIntoView(true);", target_element)

                for i in range(15):  # 15 étapes de défilement
                    time.sleep(0.5)
                    row_table = wait.until(EC.visibility_of_element_located((By.ID, f"A4_{i + 1}")))
                    row_table.click()
                    show_details_row = wait.until(EC.visibility_of_element_located((By.ID, "A20")))
                    show_details_row.click()
                    row_ferme = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='A28']")))
                    row_ferme.click()

            next_page_button = driver.find_element(By.ID, "A43")
            next_page_button.click()
        except (TimeoutException, NoSuchElementException):
            print("Aucun nouvel élément trouvé ou une étape a pris trop de temps.")
            break
    print(driver.page_source)
    time.sleep(2)
    driver.quit()
