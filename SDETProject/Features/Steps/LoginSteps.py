from behave import *
from selenium import webdriver
import time

@given(u'launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="C:/Software/chromedriver/chromedriver.exe")


@when(u'open html page')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5000/")
    time.sleep(2)


@when(u'enter Name "Neha F" UID "U100" Company Name "UST" Email "nehafc@ust.com"')
def step_impl(context):
    context.driver.find_element_by_id("name").send_keys("Lal Q")
    time.sleep(2)
    context.driver.find_element_by_id("uidd").send_keys("U952")
    time.sleep(2)
    context.driver.find_element_by_id("cnamee").send_keys("UST")
    time.sleep(2)
    context.driver.find_element_by_id("cemailid").send_keys("lal@ust.com")
    time.sleep(2)



@when(u'click on login button')
def step_impl(context):
    context.driver.find_element_by_xpath("/html/body/div/form/center/left/input").click()
    time.sleep(2)


@then(u'user must successfully login to Display page')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5000/")
    time.sleep(2)


@then(u'close browser')
def step_impl(context):
  context.driver.close()