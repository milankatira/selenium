from selenium import webdriver
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.codewithharry.com/")
print(driver.title)
driver.maximize_window()
driver.minimize_window()
driver.quit()
