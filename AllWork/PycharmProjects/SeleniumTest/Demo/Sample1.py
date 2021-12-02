from selenium import webdriver
from selenium.webdriver import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("java")
#driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
driver.close()
