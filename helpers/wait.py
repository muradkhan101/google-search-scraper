from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def wait_for_load(driver, by_type, selector):
    try:
        element_present = EC.presence_of_element_located((by_type, selector))
        WebDriverWait(driver, 5).until(element_present)
        return True
    except TimeoutException:
        print("Timed out waiting for page to load")
        return False
