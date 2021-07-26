from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://masterprograming.com/contact-us/")

#is_displayed
var=driver.find_element_by_class_name("search-field")
print(var.is_displayed())

#is_enable
var2=driver.find_element_by_name('s')
print(var2.is_enabled())
time.sleep(2)


#is_selected
driver.get("https://www.w3schools.com/html/html_forms.asp")
var3=driver.find_element_by_id('html')
print(var3.is_selected())
driver.quit()
#class="search-field" placeholder="Search …" value="" name="s"