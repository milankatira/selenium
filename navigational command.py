from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get("https://www.codewithharry.com/")
print(driver.title)

time.sleep(2)

driver.get("https://google.com/")
print(driver.title)
time.sleep(2)
driver.back()


print(driver.title)
driver.forward()
driver.quit()