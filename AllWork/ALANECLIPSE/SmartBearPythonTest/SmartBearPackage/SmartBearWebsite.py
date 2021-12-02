'''
Created on 24-Nov-2021

@author: lapto
'''
from selenium import webdriver 
from selenium.webdriver.support.ui import Select
print("test case started")  
driver = webdriver.Chrome()  
driver.maximize_window()  
driver.get("http://secure.smartbearsoftware.com/samples/testcomplete11/WebOrders/login.aspx")
driver.find_element_by_id("ctl00_MainContent_username").send_keys("Tester")
driver.find_element_by_id("ctl00_MainContent_password").send_keys("test")
driver.find_element_by_id("ctl00_MainContent_login_button").click()
driver.find_element_by_id("ctl00_MainContent_btnCheckAll").click()
driver.find_element_by_id("ctl00_MainContent_btnDelete").click()
driver.find_element_by_id("ctl00_MainContent_orderLInk").click()
driver.back();
driver.back();
driver.find_element_by_id("ctl00_MainContent_btnUncheckAll").click()
driver.find_element_by_id("ctl00_MainContent_orderGrid_ctl02_OrderSelector").click()
driver.find_element_by_id("ctl00_MainContent_btnUncheckAll").click()
     
        
        
    
driver.find_element_by_link_text("View all products").click()
driver.find_element_by_partial_link_text("Order").click()
dropdown = Select(driver.find_element_by_id("ctl00_MainContent_fmwOrder_ddlProduct"))  
dropdown.select_by_visible_text("FamilyAlbum")  
      
driver.find_element_by_css_selector("#ctl00_MainContent_fmwOrder_txtQuantity").send_keys("1000")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_txtUnitPrice").send_keys("80")
driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]").click()
driver.find_element_by_name("ctl00$MainContent$fmwOrder$txtName").send_keys("Alan Francis Cheeramvelil")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox2").send_keys("ABC")

driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox3").send_keys("kottayam")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox4").send_keys("Kerala")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox5").send_keys("686543")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_cardList_0").click()
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox6").send_keys("123456789012")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox1").send_keys("01/99")
driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/div/a").click()

drop =Select(driver.find_element_by_id("ctl00_MainContent_fmwOrder_ddlProduct"))
drop.select_by_visible_text("ScreenSaver");  
driver.find_element_by_id("ctl00_MainContent_fmwOrder_txtQuantity").send_keys("1000")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_txtUnitPrice").send_keys("80")
driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]").click()
driver.find_element_by_id("ctl00_MainContent_fmwOrder_txtName").send_keys("Alan")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox2").send_keys("Alappey")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox3").send_keys("ANC")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox4").send_keys("Kerala")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox5").send_keys("689574")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_cardList_0").click()
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox6").send_keys("123456789012")
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox1").send_keys("01/99")
driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/div/input").click()
driver.close();
    

