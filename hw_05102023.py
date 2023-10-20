from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://anc.ua/")

cookie_message = driver.find_element(By.XPATH, '//button[@class="button button-default button-blue col-2-12 col-5-12-s"]')
cookie_message.click()
chat_bot = driver.find_element(By.XPATH, '//div[@class="position-fixed-bottom"]//button')
chat_bot.click()

promotions0 = WebDriverWait(driver, 10).until_not(
    EC.visibility_of_element_located((By.XPATH, '//img[@src="https://storage.googleapis.com/static-storage/banners/desktop-webp/69e91b46-2b54-4812-9968-4500321bcdf9"]'))
    )
promotions7 = WebDriverWait(driver, 40).until(
    EC.visibility_of_element_located((By.XPATH, '//img[@src="https://storage.googleapis.com/static-storage/banners/desktop-webp/72e4ae50-5279-4c80-85a6-88df9bab7663"]'))
    )

driver.quit()


