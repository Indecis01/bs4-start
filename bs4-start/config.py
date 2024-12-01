from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait

# Edge WebDriver
service = Service(r'C:\Users\HP\Downloads\edgedriver_win64\msedgedriver.exe')
options = Options()
options.add_argument("--start-maximized")  # Ouvre Edge en mode maximisé

# Initialiser Edge avec WebDriver
driver = webdriver.Edge(service=service, options=options)
wait = WebDriverWait(driver, 20)
