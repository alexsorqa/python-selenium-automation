from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(executable_path= "./chromedriver.exe")
driver.maximize_window()

open_amazon = driver.get('https://www.amazon.com/')
sleep(1.5)
sign_in_pop_up_button = driver.find_element(By.XPATH, "//div[@id = 'nav-signin-tooltip']/a[@class = 'nav-action-button']").click()
sign_in_header = driver.find_element(By.XPATH, "//h1[@class = 'a-spacing-small']").text
print(sign_in_header)
input_field = driver.find_element(By.ID, "ap_email")

#Verify Sign in header is visible:
assert "Sign in" == sign_in_header, f'Expected "Sign in", but got actual {sign_in_header}'

#Verify email input field is present:
print("Input field is visible" if input_field else False)

driver.quit()







