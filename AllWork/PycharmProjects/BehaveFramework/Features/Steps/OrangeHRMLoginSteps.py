from behave import *
from selenium import webdriver
#@given('launch chrome browser')
#def step_impl(context):
  #  context.driver = webdriver.Chrome(executable_path="C:/Software/chromedriver/chromedriver.exe")
#@when(u'open orange hrm homepage')
#def step_impl(context):
  #  context.driver.get("https://opensource-demo.orangehrmlive.com/")

@when(u'enter username "Admin" password "admin123"')
def step_impl(context):
    context.driver.find_element_by_id("txtUsername").send_keys("Admin")
    context.driver.find_element_by_id("txtPassword").send_keys("admin123")





@when(u'click on login button')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()


@then(u'user must successfully login to Dashboard page')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
