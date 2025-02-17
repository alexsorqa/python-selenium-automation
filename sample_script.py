from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# init driver
<<<<<<< HEAD
service = Service('/Users/asorokin/Desktop/careerist/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)
=======
driver = webdriver.Chrome(executable_path= '/Users/asorokin/Desktop/careerist/python-selenium-automation/chromedriver')
>>>>>>> ee43ac350a6216d68391d8c38be3f8a15db9a7d2
driver.maximize_window()
driver.wait = WebDriverWait(driver, 10)

driver.implicitly_wait(5)  # check every 100 ms

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')), message='Search btn not clickable!')  # checks for condition to be net every 500 ms

# click search
driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
