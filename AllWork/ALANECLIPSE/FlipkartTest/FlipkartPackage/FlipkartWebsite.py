from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
print("test case started")  
#open Google Chrome browser  
driver = webdriver.Chrome("C://Software//chromedriver//chromedriver.exe")  
#maximize the window size  
driver.maximize_window()  
#delete the cookies  
driver.delete_all_cookies()  
#navigate to the url  
driver.get("https://www.flipkart.com/")  
 
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
driver.find_element_by_name("q").send_keys("shoes")  
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()
time.sleep(2)  

driver.get("https://www.flipkart.com/port-running-shoes-men/p/itm13060ed10fcbe?pid=SHOFP98ZYPDWCGSM&lid=LSTSHOFP98ZYPDWCGSMSMCNYZ&marketplace=FLIPKART&q=shoes&store=osp&srno=s_1_5&otracker=search&otracker1=search&fm=SEARCH&iid=824e261b-19c9-4d0d-a3e4-56d004da582f.SHOFP98ZYPDWCGSM.SEARCH&ppt=hp&ppn=homepage&ssid=fbkpiqjmb40000001637741649897&qH=b0a8b6f820479900")
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[5]/div/div[2]/div[1]/ul/li[5]/a").click()
time.sleep(2)


driver.find_element_by_css_selector("#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-5-12._78xt5Y > div:nth-child(2) > div > ul > li:nth-child(1) > button").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div/form/button").click()
time.sleep(2)
driver.close()  
print("successfully completed")
