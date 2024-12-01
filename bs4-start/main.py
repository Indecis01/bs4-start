from config import driver, wait
from login import login
from actions import perform_actions

def main():
    url = "https://www.mentorassurances.com/sipromedas"
    login(url, driver, wait)
    perform_actions(driver, wait)

if __name__ == "__main__":
    main()
